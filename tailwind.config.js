/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './apps/**/templates/**/*.html',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
        },
        // Cyberpunk theme colors
        cyber: {
          cyan: '#00d9ff',
          purple: '#b537f2',
          pink: '#ff006e',
          dark: '#0a0e27',
          'dark-secondary': '#1a1f3a',
          card: 'rgba(26, 31, 58, 0.8)',
          text: '#e0e7ff',
          'text-secondary': '#a0aec0',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['Fira Code', 'monospace'],
        sora: ['Sora', 'sans-serif'],
        jetbrains: ['JetBrains Mono', 'monospace'],
      },
      boxShadow: {
        'glow-cyan': '0 0 20px rgba(0, 217, 255, 0.5)',
        'glow-cyan-lg': '0 0 40px rgba(0, 217, 255, 0.4)',
        'glow-purple': '0 0 20px rgba(181, 55, 242, 0.5)',
        'glow-purple-lg': '0 0 40px rgba(181, 55, 242, 0.4)',
        'glow-mixed': '0 10px 40px rgba(0, 217, 255, 0.3), 0 0 20px rgba(181, 55, 242, 0.2)',
      },
      backgroundImage: {
        'gradient-cyber': 'linear-gradient(135deg, #00d9ff 0%, #b537f2 100%)',
        'gradient-cyber-dark': 'linear-gradient(135deg, rgba(0, 217, 255, 0.1) 0%, rgba(181, 55, 242, 0.1) 100%)',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}