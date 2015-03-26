require.config({
    baseUrl: '/static',
    paths: {
        jquery: '/vendor/jquery',
        backbone: 'vendor/backbone',
        underscore: 'underscore',
        app: 'js/app'
    },
    shim: {
        'underscore': {
            exports: '_'
        },      
        'backbone': {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        }
    }
});

