<?php
header('Content-Type: application/json; charset=utf-8');

 = file_get_contents('php://input');
 = json_decode(, true);
if (!) {
     = ;
}

 = trim(['name'] ?? '');
 = trim(['resumeText'] ?? '');
 = trim(['careerGoal'] ?? '');

if ( === '' ||  === '' ||  === '') {
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'message' => 'Please provide your name, current resume summary, and target career path.',
    ]);
    exit;
}

require_once __DIR__ . '/api_client.php';

 = sendInferenceRequest([
    'name' => ,
    'resumeText' => ,
    'careerGoal' => ,
]);

if (! || !isset(['success'])) {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'message' => 'Unable to connect to the inference service. Start the Python server at ai_engine/inference.py.',
    ]);
    exit;
}

echo json_encode();
