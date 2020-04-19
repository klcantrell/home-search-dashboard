import express from 'express';
import {
  MonthlyPaymentParameters,
  calculateMonthlyPayment,
} from './calculations';

const app = express();

app.use(express.json());

type HouseRequestBody = MonthlyPaymentParameters;

type HouseResponseBody = {
  monthlyPayment: number;
};

app.get('/health', (_, res) => {
  res.send(200);
});

app.post('/house', (req, res) => {
  const { value, downPayment, rate, term } = req.body as HouseRequestBody;

  const monthlyPayment = calculateMonthlyPayment({
    value,
    downPayment,
    rate,
    term,
  });

  res.json({
    monthlyPayment,
  } as HouseResponseBody);
});

app.listen('3000', () => {
  console.log('Listening on port 3000!');
});
