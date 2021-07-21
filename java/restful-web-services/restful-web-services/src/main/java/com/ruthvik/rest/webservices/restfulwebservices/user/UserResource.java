package com.ruthvik.rest.webservices.restfulwebservices.user;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserResource {
	
	@Autowired
	private  UserDaoService services;

	@GetMapping("/users")
	public  List<User> retriveAllUsers() {
		return services.findAll();
	}
	
	@GetMapping("/users/{id}")
	public User retrieveUser(@PathVariable int id){
		return services.findOne(id);
	}
	
	@PostMapping("/users")
	public  void createUsers(@RequestBody User user) {
		User savedUser = services.save(user);
	}
}
