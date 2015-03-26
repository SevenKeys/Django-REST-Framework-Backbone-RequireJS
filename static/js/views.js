require(['vendor/jquery','vendor/backbone','underscore','js/app'], function ($, Backbone, _, app) {

    var TemplateView = Backbone.View.extend({
        templateName: '',
        initialize: function () {
            this.template = _.template($(this.templateName).html());
        },
        render: function () {
            var context = this.getContext(),
            html = this.template(context);
            this.$el.html(html);
        },
        getContext: function () {
            return {};
        }
    });
    
    
    var HomepageView = TemplateView.extend({
        templateName: '#home-template',
        initialize: function (options) {
            var self = this;
            TemplateView.prototype.initialize.apply(this, arguments);
            app.collections.ready.done(function () {
                app.articles.fetch({
                    data: {},
                    success: $.proxy(self.render, self)
                });
            });
        },
        getContext: function () {
            return {articles: app.articles || null};
        },
    });
    

    var LoginView = TemplateView.extend({
        id: 'login',
        templateName: '#login-template',
        events: {
            'submit form': 'submit'
        },
        submit: function (event) {
            var data = {};
            event.preventDefault();
            this.form = $(event.currentTarget);
            data = {
                username: $(':input[name="username"]', this.form).val(),
                password: $(':input[name="password"]', this.form).val()
            };
            $.post(app.apiLogin, data)
            .success($.proxy(this.loginSuccess, this))
            .fail($.proxy(this.loginFailure, this));
        },
        loginSuccess: function (data) {
            app.session.save(data.token);
            this.trigger('login', data.token);
            this.remove();
        },
        loginFailure: function (xhr, status, error) {
            var errors = xhr.responseJSON;
            this.showErrors(errors);
        },
        showErrors: function (errors) {
        }
    });
    
    var HeaderView = TemplateView.extend({
        tagName: 'header',
        templateName: '#header-template',
        events: {
            'click a.logout': 'logout'
        },
        getContext: function () {
            return {authenticated: app.session.authenticated()};
        },
        logout: function (event) {
            event.preventDefault();
            app.session.delete();
            window.location = '/';
        }
    });

    
    app.views.HomepageView = HomepageView;
    app.views.LoginView = LoginView;
    app.views.HeaderView = HeaderView;
    
});