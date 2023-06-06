module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("css");
  console.log("Building for : " + process.env.NODE_ENV_POEMS);
  eleventyConfig.addGlobalData('base_url', process.env.NODE_ENV_POEMS === 'production' ? 'https://hassan-theitguy.github.io/poems/' : 'http://localhost:8080/');
  return {
	  dir: {
      output: "../docs"
    }
  };
};

