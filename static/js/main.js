const vm = new Vue ({
    el: '#app',
    data: {
        page: {}
    },
    delimiters: ['!{','}'],
    beforeMount(){
        this.page = JSON.parse(document.getElementsByTagName('table')[0].getAttribute('data') || '{}');
    },
})
