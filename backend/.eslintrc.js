module.exports = {
  parser: '@typescript-eslint/parser', // Specifies the ESLint parser
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'prettier/@typescript-eslint',
    'plugin:prettier/recommended',
  ],
  settings: {},
  env: {
    browser: true,
    node: true,
    es2017: true,
  },
  plugins: ['@typescript-eslint', 'prettier'],
  parserOptions: {
    sourceType: 'module', // Allows for the use of imports
  },
  rules: {
    '@typescript-eslint/explicit-function-return-type': 'off',
    strict: 'warn',
  },
};
