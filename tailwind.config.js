/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/templates/**/*.html',
    './app/templates/**/**/*.html',
    './app/templates/*.html',
    './node_modules/flowbite/**/*.js',
  ],
  
  theme: {
    extend: {},
  },
  plugins: [
    "./node_modules/flowbite/**/*.js",
  ],
};