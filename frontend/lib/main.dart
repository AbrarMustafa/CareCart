// main.dart

import 'package:flutter/material.dart';
import 'login_screen.dart'; // Import your login screen

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Care Cart',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: LoginScreen(), // Start with your login screen
    );
  }
}
