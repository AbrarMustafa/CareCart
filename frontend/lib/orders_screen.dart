// orders_screen.dart

import 'package:flutter/material.dart';
import 'package:frontend/create_order.dart';
import 'package:frontend/order_detail_screen.dart';
import 'api_service.dart';
import 'models.dart';

class OrdersScreen extends StatefulWidget {
  final User user; // Pass the logged-in user to this screen

  OrdersScreen({required this.user});

  @override
  _OrdersScreenState createState() => _OrdersScreenState();
}

class _OrdersScreenState extends State<OrdersScreen> {
  final ApiService apiService = ApiService();
  late Future<List<Order>> ordersFuture;

  @override
  void initState() {
    super.initState();
    refreshOrders();
  }

  void refreshOrders() {
    ordersFuture = apiService.fetchOrders();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Orders'),
        actions: [
          IconButton(
            icon: Icon(Icons.refresh),
            onPressed: () {
              refreshOrders();
            },
          ),
        ],
      ),
      body: FutureBuilder<List<Order>>(
        future: ordersFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return Center(child: Text('No orders found'));
          } else {
            return ListView.builder(
              itemCount: snapshot.data!.length,
              itemBuilder: (context, index) {
                Order order = snapshot.data![index];
                return ListTile(
                  title: Text(order.address),
                  subtitle: Text('ID: ${order.id}'),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => OrderDetailsScreen(order: order), // Navigate to order details screen
                      ),
                    );
                  },
                );
              },
            );
          }
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => CreateOrderScreen(widget.user), // Navigate to create order screen
            ),
          );
        },
        child: Icon(Icons.add),
      ),
    );
  }
}
