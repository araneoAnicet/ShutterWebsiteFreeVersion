new Vue({
    el: '#root',
    delimiters: [
        '[[', ']]'
    ],
    data: {
        message: 'Hello from vue!',
        is_spinning: true,
        is_signed_in: false,
        username: 'username'
    },
    methods: {
        show_spinner() {
            this.is_spinning = true
        },

        hide_spinner() {
            this.is_spinning = false
        },

        set_signed_in() {
            this.is_signed_in = true
        },

        set_signed_out() {
            this.is_signed_in = false
        }
    }
});

