/*

filter_home_page = new Vue({
	delimiters: ['<%', '%>'],
	el: '#app',
	data: {
		user : '',
		users: '',
	},
	created: function(){
		this.loadLoot()
	},
	methods: {
			loadLoot(){
				$.ajax({
					url: "/home/",				
					type: "POST",
					dataType: 'json',
					success: (response) => {
						this.loots = response
						console.log(response)
					}
				})
			}
		},

	computed: {
		filteredPerson: function(){
			var self = this;
			return this.userList.filter(function(user){
				return user.name.toLowerCase().indexOf(self.search.toLowerCase()) != -1 && user.city.toLowerCase().indexOf(self.search_city.toLowerCase()) != -1;
			});
		}
	}
})*/