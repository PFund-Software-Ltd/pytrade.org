const PypiBadge = ({ pypiName }) => {
  return (
    <div style={{display: 'inline-flex', alignItems: 'center', gap: '4px'}}>
      <a href={`https://pypi.org/project/${pypiName}`}><img src={`https://img.shields.io/pypi/v/${pypiName}.svg`} alt="PyPI" /></a>
      <img src={`https://img.shields.io/pypi/dm/${pypiName}?label=downloads`} alt="PyPI downloads" />
      <img src={`https://img.shields.io/pypi/pyversions/${pypiName}`} alt="PyPI - Support Python Versions" />
    </div>
  );
};

export default PypiBadge;