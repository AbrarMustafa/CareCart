// api_service.dart

import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:frontend/orders_screen.dart';
import 'package:http/http.dart' as http;
import 'models.dart';

class ApiService {
  static const String baseUrl = 'http://localhost:8000';

  Future<List<Order>> fetchOrders() async {
    final response = await http.get(Uri.parse('$baseUrl/orders/'));
    if (response.statusCode == 200) {
      List<dynamic> data = jsonDecode(response.body);
      return data.map((json) => Order.fromJson(json)).toList();
    } else {
      throw Exception('Failed to fetch orders');
    }
  }

  Future<Order> createOrder(Order order) async {
    final response = await http.post(
      Uri.parse('$baseUrl/orders/'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(order.toJson()),
    );
    if (response.statusCode == 200) {
      return Order.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Failed to create order');
    }
  }

  Future<bool> loginUser(BuildContext context, String userName, String password) async {
    final response = await http.post(
      Uri.parse('$baseUrl/verify-user/'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode({'username': userName, 'password': password}),
    );

    if (response.statusCode == 200  ) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => OrdersScreen()),
      );
      return true;
    } else {
      throw Exception('Login failed');
    }
  }


// Implement update and delete methods for orders and users
}
