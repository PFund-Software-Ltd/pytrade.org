import Image from "next/image";

export default {
    logo: (
      <>
        <Image
          src={"/logo.png"}
          priority={true}
          alt="PyTrade.org Logo"
          width={72}
          height={72}
        />
        <span style={{ fontWeight: 'bold', fontFamily: 'Futura', fontSize: '28px' }}>
          <text style={{color: '#306998'}}>
            Py
          </text>
          <text style={{color: '#FFD43B'}}>
            Trade
          </text>
        </span>
      </>
    ),
    // faviconGlyph: "PT",
    head: (
      <>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="description" content="A comprehensive collection of algorithmic trading libraries and tools in Python." />
        <meta property="og:title" content="PyTrade.org" />
        <meta property="og:description" content="Curated algo-trading libraries in Python" />
        {/* tell search engines what the "preferred" version of a webpage is */}
        <link rel="canonical" href="https://pytrade.org/" /> 
        <link rel="icon" href="/favicon.ico" />
        {/* <!-- Google tag (gtag.js) --> */}
        <script async src={`https://www.googletagmanager.com/gtag/js?id=${process.env.NEXT_PUBLIC_GA_TRACKING_ID}`}></script> 
        <script dangerouslySetInnerHTML={{
          __html: `
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', ${process.env.NEXT_PUBLIC_GA_TRACKING_ID});
          `,
        }}></script>
      </>
    ),
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