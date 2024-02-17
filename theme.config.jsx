export default {
    logo: (
      <span style={{ fontWeight: 'bold', fontFamily: 'Futura', fontSize: '28px' }}>
        <text style={{color: '#306998'}}>
          Py
        </text>
        <text style={{color: '#FFD43B'}}>
          Trade
        </text>
      </span>
    ),
    faviconGlyph: "PT",
    project: {
      link: 'https://github.com/PFund-Software-Ltd/pytrade.org'
    },
    feedback: {
        content: null,  // disable "Question? Give us feedback →"
    },
    docsRepositoryBase: 'https://github.com/PFund-Software-Ltd/pytrade.org',
    sidebar: {
        toggleButton: true,
    },
    footer: {
        component: null,  // disable footer
    },
    useNextSeoProps: () => ({
    }),
    // ... other theme options
  }