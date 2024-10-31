module.exports = {
  purge: {
    enabled: true,
    content: ["./src/**/*.html", "./src/**/*.ts"],
  },
  theme: {
    extend: {
      screens: {
        'sm900': '900px',
      },
    },
  },
  variants: {},
  plugins: [],
};
