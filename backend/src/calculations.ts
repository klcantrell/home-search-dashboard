export type MonthlyPaymentParameters = {
  value: number;
  downPayment: number;
  rate: number;
  term: number;
};

const MONTHS_IN_YEAR = 12;

export const calculateMonthlyPayment = ({
  value,
  downPayment,
  rate,
  term,
}: MonthlyPaymentParameters) => {
  const principalLoanAmount = value - downPayment;
  const monthlyRate = rate / 100 / MONTHS_IN_YEAR;
  const numberOfPayments = term * MONTHS_IN_YEAR;
  const monthlyPaymentRaw =
    principalLoanAmount *
    ((monthlyRate * Math.pow(1 + monthlyRate, numberOfPayments)) /
      (Math.pow(1 + monthlyRate, numberOfPayments) - 1));
  const monthlyPayment = Math.round(monthlyPaymentRaw * 100) / 100;
  return monthlyPayment;
};
