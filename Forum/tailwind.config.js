// tailwind.config.js
module.exports = {
    theme: {
      extend: {
        keyframes: {
          jump: {
            '0%, 100%': { transform: 'translateY(0) scale(1)' },
            '50%': { transform: 'translateY(-5px) scale(1.1)' },
          },
        },
        animation: {
          jump: 'jump 1s ease-in-out infinite',
        },
      },
    },
    plugins: [],
  }
  