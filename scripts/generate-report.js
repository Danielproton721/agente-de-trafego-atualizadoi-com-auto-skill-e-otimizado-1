// Gera relatório final
const fs = require('fs');
const path = require('path');

const DEFAULT_SESSION_DIR = 'Conhecimento/Referencias/Keyword-Research/2026-05-21-achados-churrasco-perfume-arabe-idoso';
const sessionDir = path.resolve(process.argv[2] || process.env.KEYWORD_RESEARCH_DIR || DEFAULT_SESSION_DIR);
const dataDir = path.join(sessionDir, 'dados');
const approved = JSON.parse(fs.readFileSync(path.join(dataDir, 'kw-approved.json'), 'utf8'));

const tierLabel = { 'A++': 'A++ (1M+)', 'A': 'A (100k-1M)', 'B+': 'B+ (30-100k)', 'B': 'B (10-30k*)' };

// Tabela completa
let md = '';
md += '| Tier | Camada | Palavra | Volume mensal (BR) | Competition | CPC low (BRL) | CPC high (BRL) | Categoria | Observação |\n';
md += '|------|--------|---------|--------------------|-------------|---------------|-----------------|-----------|------------|\n';
for (const a of approved) {
  const obs = [];
  if (a.m3 && a.m3 !== '0%' && a.m3 !== '0') obs.push('Δ3m=' + a.m3);
  if (a.yoy && a.yoy !== '0%' && a.yoy !== '0') obs.push('YoY=' + a.yoy);
  md += `| ${a.tier} | ${a.camada} | ${a.kw} | ${a.vol} | ${a.conc} | ${a.cpcLow} | ${a.cpcHigh} | ${a.categoria} | ${obs.join(' ')} |\n`;
}

fs.writeFileSync(path.join(sessionDir, 'tabela-completa.md'), md);

// Top 15 oportunidades gerais (mix de volume alto + competition não-Alta preferível)
const score = (a) => {
  let s = 0;
  if (a.tier === 'A++') s += 100;
  else if (a.tier === 'A') s += 50;
  else if (a.tier === 'B+') s += 25;
  else if (a.tier === 'B') s += 10;
  if (a.conc === 'Baixa') s += 30;
  else if (a.conc === 'Média') s += 15;
  if (a.camada === 1) s += 5;
  return s;
};

const sorted = [...approved].sort((a, b) => score(b) - score(a));

console.log('=== TOP 15 OPORTUNIDADES GERAIS ===');
sorted.slice(0, 15).forEach((a, i) => console.log(`${i+1}. ${a.kw} | ${a.vol} | ${a.conc} | CPC ${a.cpcLow}-${a.cpcHigh} | ${a.categoria} | C${a.camada}`));

console.log('\n=== TOP 10 NICHOS CAMADA 3 ===');
approved.filter(a => a.camada === 3).slice(0, 10).forEach((a, i) => console.log(`${i+1}. ${a.kw} | ${a.vol} | ${a.conc} | ${a.categoria}`));

console.log('\n=== TOP 10 PRODUTOS CAMADA 2 (maior volume) ===');
approved.filter(a => a.camada === 2).filter(a => a.tier === 'A++' || a.tier === 'A').slice(0, 10).forEach((a, i) => console.log(`${i+1}. ${a.kw} | ${a.vol} | ${a.conc} | ${a.categoria}`));

console.log('\n=== KEYWORDS COM COMPETIÇÃO BAIXA OU MÉDIA (potencial ouro) ===');
const lowComp = approved.filter(a => a.conc === 'Baixa' || a.conc === 'Média');
console.log('Total com Comp Baixa/Média:', lowComp.length);
lowComp.forEach(a => console.log(`- ${a.kw} | ${a.vol} | ${a.conc} | CPC ${a.cpcLow}-${a.cpcHigh} | ${a.categoria} | C${a.camada}`));

console.log('\n=== KEYWORDS COM SINAL DE TENDÊNCIA (Δ3m ou YoY ≠ 0) ===');
const trending = approved.filter(a => (a.m3 && a.m3 !== '0%' && a.m3 !== '0') || (a.yoy && a.yoy !== '0%' && a.yoy !== '0'));
console.log('Total com sinal:', trending.length);
trending.slice(0, 20).forEach(a => console.log(`- ${a.kw} | ${a.vol} | Δ3m=${a.m3} | YoY=${a.yoy} | ${a.categoria}`));

console.log('\n=== TIER A++ COMPLETO ===');
approved.filter(a => a.tier === 'A++').forEach(a => console.log(`- ${a.kw} | ${a.vol} | ${a.conc} | ${a.categoria}`));
