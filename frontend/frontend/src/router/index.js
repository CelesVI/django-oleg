
import Vue from 'vue'
import Router from 'vue-router'

import Create from '../views/Create.vue'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/create',
            name: 'create',
            component: Create
        }
    ]
})
