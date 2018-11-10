var app = new Vue ({
    el: '#icon',
    data: {
        fafa: "fa fa-check"
    },
    delimiters: ['!{','}'],
    computed: {
        fafaa() {
            if (this.item.status == "SUCCESS") {
            return "fa fa-check"
            } else if (this.item.status == "CRASH") {
            return "fa fa-remove"
            } else {
            return "fa fa-minus"
            }
        }
    }
})