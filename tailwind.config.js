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
      colors: {
        'primary': '#000000',
        'secondary': '#ffffff',
      },
    },
  },
  variants: {},
  plugins: [
    require('@tailwindcss/aspect-ratio'),
  ],
};
