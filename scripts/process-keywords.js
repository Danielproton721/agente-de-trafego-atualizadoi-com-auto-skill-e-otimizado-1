// Consolida 3 batches, deduplica, filtra e classifica
const fs = require('fs');
const path = require('path');

const DEFAULT_SESSION_DIR = 'Conhecimento/Referencias/Keyword-Research/2026-05-21-achados-churrasco-perfume-arabe-idoso';
const sessionDir = path.resolve(process.argv[2] || process.env.KEYWORD_RESEARCH_DIR || DEFAULT_SESSION_DIR);
const dataDir = path.join(sessionDir, 'dados');

const batches = [
  'kw-batch1-sorted.json',
  'kw-batch2-sorted.json',
  'kw-batch3-sorted.json'
].map((name) => path.join(dataDir, name));

// Volume tier mapping. Parseia o LIMITE INFERIOR da faixa do Keyword Planner.
function parseUnit(num, unit) {
  const n = parseFloat(num.replace(',', '.'));
  if (!unit) return n;
  const u = unit.toLowerCase().trim();
  if (u === 'mi') return n * 1_000_000;
  if (u === 'mil') return n * 1_000;
  return n;
}
function volumeToTier(vol) {
  if (!vol) return null;
  // Split por traço (en-dash, em-dash, hyphen)
  const parts = vol.split(/\s*[–—-]\s*/);
  if (parts.length < 2) return null;
  // Pega o LIMITE INFERIOR (primeira parte). Ex: "10 mil" da faixa "10 mil – 100 mil"
  const low = parts[0].trim();
  const m = low.match(/^([\d.,]+)\s*(mi|mil)?$/i);
  if (!m) return null;
  const lowVal = parseUnit(m[1], m[2]);
  if (lowVal >= 1_000_000) return 'A++';   // 1M+ buscas
  if (lowVal >= 100_000) return 'A';        // 100k-1M
  if (lowVal >= 30_000) return 'B+';        // 30k-100k (TIER B do SOP)
  if (lowVal >= 10_000) return 'B';         // 10k-30k (TIER C do SOP — nicho)
  return null;                              // <10k descarta
}

// Vendabilidade - palavras a EXCLUIR
const EXCLUDE_PATTERNS = [
  // Marcas isoladas/produto específico de marca (mantém quando vem c/ categoria)
  /^(samsung|apple|xiaomi|motorola|lenovo|dell|acer|asus|nike|adidas|puma|vans|olympikus|brastemp|electrolux|panasonic|consul|midea|pampers|huggies|johnson)$/i,
  // Conteúdo informacional
  /^(como|onde|quando|por que|porque|o que|qual|significado|receita|tutorial|aprenda)/i,
  // Lugares/marketplace específico
  /(magazine luiza|magalu|amazon|mercado livre|americanas|shopee|aliexpress|kabum|pichau|casas bahia)/i,
  // Termos de info/conteúdo
  /(letra|musica|filme|série|episódio|temporada|trailer|sinopse|elenco|ator|atriz)/i,
  // Conteúdo de notícia/politico
  /(noticia|política|eleição|presidente|governo|stf|lula|bolsonaro)/i,
  // Termos suspeitos
  /(porno|sex|adulto|cassino|aposta|bet|sportingbet)/i,
];

// Nomes próprios de perfumes/produtos de marca específica
const BRAND_PRODUCTS = [
  /^(la vie est belle|good girl|miss dior|angel|coco mademoiselle|j'adore|black opium|paco rabanne|1 million|invictus|sauvage|bleu de chanel|olympea)/i,
  /^(galaxy watch|apple watch|samsung watch|xiaomi watch|amazfit|garmin)\b/i,
  /(iphone|macbook|airpods)/i,
];

function isVendableOnline(kw) {
  const k = kw.toLowerCase().trim();
  for (const p of EXCLUDE_PATTERNS) if (p.test(k)) return false;
  for (const p of BRAND_PRODUCTS) if (p.test(k)) return false;
  // Tamanho: 1-5 palavras
  const wc = k.split(/\s+/).length;
  if (wc > 5) return false;
  return true;
}

// Classifica em Camada 1/2/3
function classifyCamada(kw) {
  const k = kw.toLowerCase().trim();
  const wc = k.split(/\s+/).length;
  // Camada 1: tema-mãe (1 palavra ampla)
  const tema_mae = ['tênis','tenis','vestido','perfume','perfumes','ração','racao','celular','notebook','suplemento','churrasco','bolsa','mochila','sofá','sofa','colchão','colchao','fralda','bicicleta','smartwatch','fone','geladeira','brinquedo','vinho','café','cafe','piscina','parafuso','whey','creatina','vitamina','shampoo','maquiagem','sapato','cama','mesa','cortina','tapete','piso','tinta','pneu','bateria','óleo','filtro','farol','capacete','moto','fogão','fogao','ventilador','liquidificador','tv','console','teclado','monitor','impressora','remédio','massageador','andador','mamadeira','berço','berco','chupeta','patins','skate','halteres','academia','livro','jogo','violão','violao','caderno','caneta','agenda','planner','plantas','suculenta','churrasqueira','deck','meditação','meditacao','aromaterapia','tarô','taro','cristal','incenso'];
  if (wc === 1 && tema_mae.includes(k)) return 1;
  // Camada 2: produto específico vendável (2-3 palavras com modificador genérico)
  // ex: "sofa cama", "geladeira frost free", "tenis de corrida"
  // Camada 3: nicho segmentado (público específico)
  // ex: "ração natural", "sapato ortopédico", "suplemento idoso", "tenis feminino"
  const nicho_markers = /(feminino|masculino|infantil|idoso|baby|bebê|bebe|natural|orgânico|organico|vegano|sem gluten|sem lactose|fitness|gamer|geriátrica|geriatrica|ortopédico|ortopedico|plus size|montessori|premium|profissional|crossfit|yoga|pilates|gestante|gravidez|gravida|criança|crianca|adulto|kids|teen|low carb|high protein|isolado|hidrolisado|whey|frost free|inverter|inverse|side by side|automático|automatico|desmontável|desmontavel|portátil|portatil|gourmet|tinto|branco|rosé|seco|suave)/i;
  if (nicho_markers.test(k)) return 3;
  // Default: Camada 2
  return 2;
}

// Categoria geral
function categoria(kw) {
  const k = kw.toLowerCase();
  if (/(tênis|tenis|sapato|chinelo|sandália|sandalia|bota|scarpin|crocs|sapatilha)/.test(k)) return 'Calçados';
  if (/(vestido|saia|blusa|camisa|calça|calca|jaqueta|casaco|biquini|biquíni|short|legging|bermuda|moletom|maiô|maio|terno|fantasia|pijama|lingerie|sutiã|sutia|cueca|kimono)/.test(k)) return 'Moda';
  if (/(bolsa|mochila|carteira|cinto|boné|bone|óculos|oculos|relógio|relogio)/.test(k)) return 'Acessórios';
  if (/(perfume|maquiagem|shampoo|esmalte|batom|base|cílios|cilios|peruca|escova|secador|chapinha|depilador|barbeador|cosmético|cosmetico|skincare|hidratante|protetor solar|sérum|serum)/.test(k)) return 'Beleza';
  if (/(suplemento|whey|creatina|vitamina|colágeno|colageno|remédio|remedio|massageador|fitoterápico|anticoncepcional|absorvente|fralda geriátrica|geriatrica)/.test(k)) return 'Saúde';
  if (/(notebook|celular|fone|geladeira|smartwatch|fogão|fogao|microondas|liquidificador|tv|televisão|televisao|console|teclado|monitor|impressora|webcam|ventilador|ar condicionado|frigobar)/.test(k)) return 'Eletrônicos';
  if (/(ração|racao|coleira|comedouro|areia higiênica|higienica|aquário|aquario|peixe ornamental|cachorro|gato|pet)/.test(k)) return 'Pet';
  if (/(sofá|sofa|colchão|colchao|cama|mesa|cortina|tapete|piso|tinta|armário|armario|guarda-roupa|estante|escrivaninha)/.test(k)) return 'Casa/Móveis';
  if (/(parafuso|ferramenta|torneira|porta|janela|telha|cimento|tijolo|furadeira|chave de fenda|broca|serra|lixadeira|rebite)/.test(k)) return 'Construção/Ferragens';
  if (/(churrasco|carne|vinho|café|cafe|pizza|sushi|açaí|acai|cerveja|chocolate|queijo|hambúrguer|hamburguer|bolo|doce|pão|pao|fruta|empório|emporio|salgado|congelado|capsulas dolce gusto)/.test(k)) return 'Alimentação';
  if (/(bicicleta|halteres|academia|patins|skate|crossfit|yoga|pilates|natação|natacao)/.test(k)) return 'Esporte';
  if (/(fralda|mamadeira|carrinho de bebê|berço|berco|chupeta|papinha|bebê|bebe|baby)/.test(k)) return 'Mãe e Bebê';
  if (/(piscina|churrasqueira|deck|jardim|vaso|planta|suculenta|espreguiçadeira|pergolado)/.test(k)) return 'Jardim/Lazer';
  if (/(cadeira gamer|mesa de escritório|planner|agenda|organizador|caderno|caneta)/.test(k)) return 'Papelaria/Escritório';
  if (/(brinquedo|jogo|board game|montessori|presente)/.test(k)) return 'Brinquedos';
  if (/(decoração|decoracao|lembrancinha|bolo|casamento|formatura|festa|batizado|balão|balao|vela)/.test(k)) return 'Festas/Decoração';
  return 'Outros';
}

// Process
const all = new Map();
batches.forEach((batchPath, idx) => {
  const b = JSON.parse(fs.readFileSync(path.resolve(batchPath), 'utf8'));
  // Skip first row (header)
  for (let i = 1; i < b.data.length; i++) {
    const r = b.data[i];
    if (!r || r.length < 9) continue;
    const kw = (r[1] || '').trim();
    if (!kw) continue;
    const vol = r[2];
    const conc = r[5];
    const cpcLow = r[7];
    const cpcHigh = r[8];
    const yoy = r[4];
    const m3 = r[3];
    // Skip duplicates
    if (all.has(kw.toLowerCase())) continue;
    all.set(kw.toLowerCase(), { kw, vol, conc, cpcLow, cpcHigh, yoy, m3, batch: idx + 1 });
  }
});

const totalRaw = all.size;

// Filter
const approved = [];
const rejected = { volume: 0, vendabilidade: 0, tamanho: 0 };
for (const item of all.values()) {
  const tier = volumeToTier(item.vol);
  if (!tier) { rejected.volume++; continue; }
  if (!isVendableOnline(item.kw)) { rejected.vendabilidade++; continue; }
  // Tamanho check (já dentro de isVendableOnline)
  item.tier = tier;
  item.camada = classifyCamada(item.kw);
  item.categoria = categoria(item.kw);
  approved.push(item);
}

// Sort: Tier (A++ -> A -> B) > Camada (1 -> 2 -> 3) > Volume (we already have ordering by volume from grid)
const tierOrder = { 'A++': 0, 'A': 1, 'B+': 2, 'B': 3 };
approved.sort((a, b) => {
  if (tierOrder[a.tier] !== tierOrder[b.tier]) return tierOrder[a.tier] - tierOrder[b.tier];
  if (a.camada !== b.camada) return a.camada - b.camada;
  return 0; // mantém ordem original (já é por relevância/volume)
});

// Output
console.log('=== STATS ===');
console.log('Total brutas:', totalRaw);
console.log('Rejeitadas por volume <10k:', rejected.volume);
console.log('Rejeitadas por vendabilidade/tamanho:', rejected.vendabilidade);
console.log('APROVADAS:', approved.length);
console.log('');
console.log('=== POR TIER ===');
['A++', 'A', 'B+', 'B'].forEach(t => {
  console.log(t + ':', approved.filter(a => a.tier === t).length);
});
console.log('');
console.log('=== POR CAMADA ===');
[1, 2, 3].forEach(c => {
  console.log('Camada ' + c + ':', approved.filter(a => a.camada === c).length);
});
console.log('');
console.log('=== POR CATEGORIA ===');
const catCount = {};
approved.forEach(a => { catCount[a.categoria] = (catCount[a.categoria] || 0) + 1; });
Object.entries(catCount).sort((a,b)=>b[1]-a[1]).forEach(([k,v]) => console.log(k + ':', v));

// Save approved
const approvedPath = path.join(dataDir, 'kw-approved.json');
fs.writeFileSync(approvedPath, JSON.stringify(approved, null, 2));
console.log('');
console.log('Saved to ' + approvedPath);
