var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
    entry: ['./src/js/main.jsx', './src/scss/main.scss'],
    output: {
        path: __dirname + '/static/',
        filename: 'main.js'
    },
    module: {

        rules: [
            {
                test: /\.(sass|scss)$/,
                loader: ExtractTextPlugin.extract(['css-loader', 'sass-loader'])
            },
            {
                test: /\.jsx$/,
                loader: 'babel-loader',
                query: {
                    presets: ['es2015', 'react']
                }
            }
        ]
    },
    stats: {
        colors: true
    },
    plugins: [
        new ExtractTextPlugin({ // define where to save the file
            filename: './[name].css',
            allChunks: true,
        })
    ],
    devtool: 'source-map'
};
