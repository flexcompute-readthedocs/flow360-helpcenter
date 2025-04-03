const getConfig = require("vuepress-bar");

let { sidebar } = getConfig({
	addReadMeToFirstGroup: false,
	mixDirectoriesAndFilesAlphabetically: false,
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
	head: [
		['meta', { 'http-equiv': 'cache-control', content: 'no-store' }],
		['meta', { 'http-equiv': 'expires', content: '0' }]
	  ]
};