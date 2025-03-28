const getConfig = require("vuepress-bar");

let { sidebar } = getConfig({
	addReadMeToFirstGroup: false,
	mixDirectoriesAndFilesAlphabetically: true,
	maxLevel: 4,
	sortByPath: true, 
});

module.exports = {
	plugins: [
		["@vuepress/plugin-back-to-top"],
		[
			"vuepress-plugin-mathjax",
			{
				target: "svg",
				macros: {
					"*": "\\times",
				},
			},
		],
	],
	themeConfig: {
		navbar: false,
		sidebar,
	},
};