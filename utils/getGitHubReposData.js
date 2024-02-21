const getReposData = async (repos) => {
  const reposData = await Promise.all(
    repos.map(async (repo) => {
      let resRepo, resContributors, resReleases;
     
      // GITHUB_TOKEN is for development only, and should not be used in production.
      const headers = process.env.GITHUB_TOKEN ? {
        'Authorization': `token ${process.env.GITHUB_TOKEN}`,
      } : {};
  
      // Fetch repo
      resRepo = await fetch(`https://api.github.com/repos/${repo}`, { headers });
      const data = await resRepo.json();
      // const pushedAtDateOnly = new Date(data.pushed_at).toISOString().split('T')[0];
      
      // Fetch contributors
      resContributors = await fetch(`https://api.github.com/repos/${repo}/contributors`, { headers });
      const dataContributors = await resContributors.json();
      const numberOfContributors = dataContributors.length;
      
      // Fetch tags for latest version
      resReleases = await fetch(`https://api.github.com/repos/${repo}/releases`, { headers });
      const dataReleases = await resReleases.json();
      const version = dataReleases.length > 0 ? dataReleases[0].name : '';
      let lastPublishedAt;
      lastPublishedAt = dataReleases.length > 0 ? dataReleases[0].published_at : '';
      // Convert lastPublishedAt to date-only format
      if (lastPublishedAt) {
        lastPublishedAt = new Date(lastPublishedAt).toISOString().split('T')[0];
      }
  
      return {
        name: data.name,
        fullName: data.full_name,
        description: data.description,
        website: data.homepage,
        stars: data.stargazers_count,
        issues: data.open_issues,
        contributors: numberOfContributors,
        publishedAt: lastPublishedAt,
        version,
        forks: data.forks,
        watchers: data.subscribers_count,
      };
    })
  );
  return {
    props: {
      // We add an `ssg` field to the page props,
      // which will be provided to the Nextra `useData` hook.
      ssg: {
        repos: reposData,
      }
    },
  };
}

export default getReposData;