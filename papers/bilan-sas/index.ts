import { PDFDocument, rgb } from 'pdf-lib';
import fs from 'fs';

type Transaction = {
  type: 'Income' | 'Expense';
  category: string;
  amount: number;
};

type FinancialSummary = {
  totalIncome: number;
  totalExpenses: number;
  netProfit: number;
  details: { [category: string]: number };
};

// Simuler les données financières
const transactions: Transaction[] = [
  { type: 'Income', category: 'Ventes', amount: 50000 },
  { type: 'Income', category: 'Autres revenus', amount: 10000 },
  { type: 'Expense', category: 'Loyer', amount: -12000 },
  { type: 'Expense', category: 'Salaires', amount: -20000 },
  { type: 'Expense', category: 'Fournitures', amount: -5000 },
];

// Calculer les totaux
const generateSummary = (transactions: Transaction[]): FinancialSummary => {
  let totalIncome = 0;
  let totalExpenses = 0;
  const details: { [category: string]: number } = {};

  for (const transaction of transactions) {
    if (transaction.type === 'Income') {
      totalIncome += transaction.amount;
    } else if (transaction.type === 'Expense') {
      totalExpenses += transaction.amount;
    }

    if (!details[transaction.category]) {
      details[transaction.category] = 0;
    }
    details[transaction.category] += transaction.amount;
  }

  return {
    totalIncome,
    totalExpenses,
    netProfit: totalIncome + totalExpenses,
    details,
  };
};

// Générer un PDF
const generatePDF = async (summary: FinancialSummary) => {
  const pdfDoc = await PDFDocument.create();
  const page = pdfDoc.addPage([600, 400]);
  const { totalIncome, totalExpenses, netProfit, details } = summary;

  const title = 'Bilan de Fin d\'Année';
  page.drawText(title, { x: 200, y: 350, size: 20, color: rgb(0, 0, 1) });

  const lines = [
    `Total des Revenus : ${totalIncome.toFixed(2)} €`,
    `Total des Dépenses : ${totalExpenses.toFixed(2)} €`,
    `Résultat Net : ${netProfit.toFixed(2)} €`,
    '',
    'Détails par catégorie :',
  ];

  let y = 320;
  for (const line of lines) {
    page.drawText(line, { x: 50, y, size: 12 });
    y -= 20;
  }

  for (const [category, amount] of Object.entries(details)) {
    page.drawText(`  - ${category} : ${amount.toFixed(2)} €`, { x: 50, y, size: 12 });
    y -= 20;
  }

  const pdfBytes = await pdfDoc.save();
  fs.writeFileSync('bilan.pdf', pdfBytes);
  console.log('PDF généré : bilan.pdf');
};

// Main
(async () => {
  const summary = generateSummary(transactions);
  await generatePDF(summary);
})();
