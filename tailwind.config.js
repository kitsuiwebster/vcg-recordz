/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,ts}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Space Grotesk', 'system-ui', 'sans-serif'],
        display: ['Space Grotesk', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'Courier New', 'Courier', 'monospace'],
      },
      fontSize: {
        xxs: '0.625rem',
        'display-sm': ['clamp(2.5rem, 5vw, 4rem)', { lineHeight: '0.95', letterSpacing: '-0.03em' }],
        'display-md': ['clamp(3rem, 8vw, 6rem)', { lineHeight: '0.9', letterSpacing: '-0.04em' }],
        'display-lg': ['clamp(4rem, 12vw, 10rem)', { lineHeight: '0.85', letterSpacing: '-0.05em' }],
        'display-xl': ['clamp(5rem, 18vw, 16rem)', { lineHeight: '0.82', letterSpacing: '-0.06em' }],
      },
      screens: {
        sm900: '900px',
      },
      colors: {
        ink: {
          0: '#000000',
          50: '#0a0a0a',
          100: '#171717',
          200: '#262626',
          300: '#404040',
          400: '#737373',
          500: '#a3a3a3',
          600: '#d4d4d4',
          700: '#e5e5e5',
          800: '#f5f5f5',
          900: '#ffffff',
        },
      },
      spacing: {
        section: '6rem',
        'section-lg': '10rem',
      },
      transitionTimingFunction: {
        editorial: 'cubic-bezier(0.22, 1, 0.36, 1)',
      },
    },
  },
  plugins: [require('@tailwindcss/aspect-ratio')],
};
