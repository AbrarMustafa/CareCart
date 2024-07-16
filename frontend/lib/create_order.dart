
import 'package:flutter/material.dart';
import 'api_service.dart';
import 'models.dart';

class CreateOrderScreen extends StatefulWidget {
  final User user; // Pass the logged-in user to this screen
  CreateOrderScreen(this.user);

  @override
  _CreateOrderScreenState createState() => _CreateOrderScreenState();
}

class _CreateOrderScreenState extends State<CreateOrderScreen> {
  final ApiService apiService = ApiService();
  late TextEditingController addressController;
  late TextEditingController contactNumberController;
  // Add controllers for other fields

  @override
  void initState() {
    super.initState();
    addressController = TextEditingController();
    contactNumberController = TextEditingController();
    // Initialize other controllers
  }

  @override
  void dispose() {
    addressController.dispose();
    contactNumberController.dispose();
    // Dispose other controllers
    super.dispose();
  }

  void createOrder() async {
    try {
      // Assuming you have controllers for address and contact number
      Order newOrder = Order(
        id: 0, // Adjust as needed based on backend behavior
        address: addressController.text,
        contactNumber: contactNumberController.text,
        note: "", // Adjust based on your UI or leave empty if not used
        createdDate: DateTime.now(), // Set current date/time or adjust as needed
        productDeliveryDate: DateTime.now(), // Set as needed
        shopperId: widget.user.id, // Assuming user is passed as a widget parameter
        cartId: 0, // Adjust based on your application logic
        userAccountId: 0,//widget.user.account.id, // Assuming user account is part of User model
        tip: 0.0, // Default tip or adjust as needed
      );

      await apiService.createOrder(newOrder);
      Navigator.pop(context);
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
        content: Text('Failed to create order: $e'),
      ));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Create Order'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            TextField(
              controller: addressController,
              decoration: InputDecoration(labelText: 'Address'),
            ),
            TextField(
              controller: contactNumberController,
              decoration: InputDecoration(labelText: 'Contact Number'),
            ),
            // Add other input fields for the order
            SizedBox(height: 16.0),
            ElevatedButton(
              onPressed: createOrder,
              child: Text('Create Order'),
            ),
          ],
        ),
      ),
    );
  }
}