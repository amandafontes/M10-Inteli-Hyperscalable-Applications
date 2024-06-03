import 'package:http/http.dart' as http;
import 'dart:convert';
import '../models/user_model.dart';

class LoginController {
  Future<String?> login(User user) async {
    final response = await http.post(
      Uri.parse('http://backend-url/auth/login'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode(user.toJson()),
    );

    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      return data['token'];
    } else {
      return null;
    }
  }
}
