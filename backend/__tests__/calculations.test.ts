import { calculateMonthlyPayment } from '../src/calculations';

it('calculates monthly mortgage according to the amortization equation', () => {
  const value = 300_000;
  const downPayment = 20_000;
  const rate = 4.2;
  const term = 30;

  const result = calculateMonthlyPayment({ value, downPayment, rate, term });

  expect(result).toBe(1369);
});
