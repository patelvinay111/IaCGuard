
| Component      | Threat                                  | Likelihood | Mitigation Strategy                                                                      |
|----------------|-----------------------------------------|------------|------------------------------------------------------------------------------------------|
| AWS S3 (Source)| Unauthorized access                     | Medium     | Implement a strict IAM policy, enable MFA, and use S3 bucket policies for fine-grained ACL|
| AWS S3 (Source)| Data leakage                            | Medium     | Use server-side encryption, access logging, and regularly review permissions              |
| Eventbridge    | Misconfiguration of event rules         | Low        | Regularly audit and monitor Eventbridge rules and settings                                |
| Amazon SNS     | Exposure of sensitive data              | Low        | Encrypt messages using AWS KMS, ensure HTTPS endpoints for subscribers                    |
| Amazon SNS     | Misdelivery of messages                 | Low        | Implement dead-letter queues and monitor delivery status of messages                     |
| Amazon SQS     | Message tampering                       | Low        | Enable SQS encryption at rest, enforce HTTPS for in-transit messages                      |
| Amazon SQS     | Overflow of messages                    | Medium     | Monitor queue size, set appropriate retention policies, and use scaling procedures        |
| AWS Lambda     | Execution of malicious code             | Medium     | Regularly update function code, review execution roles and limit their permissions        |
| AWS Lambda     | Denial of Service (DoS)                 | Low        | Set up Lambda concurrency controls and apply appropriate scaling                          |
| AWS S3 (Target)| Incomplete data transmission            | Low        | Implement data integrity checks and retry mechanisms                                     |
| AWS S3 (Target)| Accidental data overwrites/deletion     | Medium     | Enable versioning, MFA Delete feature, and cross-region replication for backup            |
