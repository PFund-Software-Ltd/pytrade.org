import nextra from 'nextra'

const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
}

const withNextra = nextra({
  theme: 'nextra-theme-docs',
  themeConfig: './theme.config.jsx'
})
 
export default withNextra(nextConfig)
 
// If you have other Next.js configurations, you can pass them as the parameter:
// module.exports = withNextra({ /* other next.js config */ })