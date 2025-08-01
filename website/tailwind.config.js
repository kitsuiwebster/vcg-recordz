module.exports = {
  content: [
    './src/**/*.{html,ts}'
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Courier New', 'Courier', 'monospace'],
      },
      screens: {
        'sm900': '900px',
      },
      fontSize: {
        'xxs': '0.625rem',
      },
    },
  },
  variants: {},
  plugins: [
    require('@tailwindcss/aspect-ratio'),
  ],
};
