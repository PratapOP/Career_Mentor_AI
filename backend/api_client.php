<?php
/**
 * Core AI Engine Communicator Function
 * Sends processed user profiles to the Python inference microservice.
 *
 * @param string $jsonPayload Pre-formatted JSON text data string
 * @return string The markdown response containing AI career advice
 */
function callAIModelMicroservice($jsonPayload) {
    // The endpoint URL where our background Python Flask API will be listening
    $url = "http://127.0.0.1:5000/api/predict";

    // 1. Initialize a cURL session handle
    $ch = curl_init($url);

    // 2. Configure our cURL session transfer options
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // Return the transfer as a string instead of outputting directly
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST"); // Use HTTP POST method
    curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonPayload); // Attach our raw JSON payload data strings
    
    // Set headers so the receiving server knows it's getting raw JSON data
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Content-Length: ' . strlen($jsonPayload)
    ]);

    // Set a safe timeout (e.g., 30 seconds) because LLM inference takes some processing time
    curl_setopt($ch, CURLOPT_TIMEOUT, 30);

    // 3. Execute the cURL network request call and grab the returned data
    $response = curl_exec($ch);

    // 4. Error Checking Layer
    if (curl_errno($ch)) {
        $errorMessage = curl_error($ch);
        curl_close($ch);
        return "CRITICAL_CONNECTION_ERROR: Failed to establish contact with the AI engine. Detailed telemetry code: " . $errorMessage;
    }

    // 5. Close the cURL resource session handle to free up web-server memory
    curl_close($ch);

    // Return the response string text back to the primary controller
    return $response;
}
?>