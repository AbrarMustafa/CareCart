// order_details_screen.dart

import 'package:flutter/material.dart';
import 'models.dart'; // Import your Order model

class OrderDetailsScreen extends StatelessWidget {
  final Order order; // Pass the selected order to display details

  OrderDetailsScreen({required this.order});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Order Details'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text('Order ID: ${order.id}'),
            Text('Address: ${order.address}'),
            Text('Contact Number: ${order.contactNumber}'),
            // Add more fields as needed
          ],
        ),
      ),
    );
  }
}
