/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./delhi/*.html",
    "./noida/*.html",
    "./blog/*.html",
    "./blog/articles/*.html",
  ],
  theme: {
    extend: {
      colors: {
        'neon-blue': '#00f3ff',
        'neon-purple': '#bc13fe',
        'deep-navy': '#050511',
        'glass': 'rgba(255, 255, 255, 0.05)',
      },
      fontFamily: {
        sans: ['Outfit', 'sans-serif'],
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
      },
      boxShadow: {
        'neon-blue': '0 0 20px rgba(0, 243, 255, 0.5)',
        'neon-purple': '0 0 20px rgba(188, 19, 254, 0.5)',
      }
    },
  },
  plugins: [],
}
