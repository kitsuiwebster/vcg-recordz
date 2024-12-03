module.exports = {
  purge: {
    enabled: true,
    content: [
      './src/**/*.{html,ts}'
    ],
  },
  theme: {
    extend: {
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
