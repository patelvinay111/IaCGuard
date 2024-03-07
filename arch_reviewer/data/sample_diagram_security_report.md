
| Component          | Threat                                       | Likelihood | Mitigation Strategy                                                                            |
|--------------------|----------------------------------------------|------------|-------------------------------------------------------------------------------------------------|
| AWS S3 (Data Source)   | Unauthorized Access                          | Medium     | Implement IAM policies; Enable S3 Bucket encryption; Use S3 access logging; Enable MFA Delete.   |
| AWS S3 (Data Source)   | Data Leakage                                 | Medium     | Enable S3 Bucket encryption; Use HTTPS for data in transit; ACLs and Policy controls.            |
| Amazon EventBridge | Misconfiguration leading to data loss         | Low        | Strictly manage IAM roles and policies; Regularly audit EventBridge rules.                       |
| Amazon EventBridge | Injection attacks through events             | Medium     | Validate event patterns; Sanitize and validate input data.                                       |
| Amazon SNS         | Unauthorized Access/Interception of Messages | High       | Use server-side encryption (SSE); Implement access control policies.                            |
| Amazon SNS         | DoS attacks by flooding topics with messages | Medium     | Configure throttling; Enable dead letter queues to manage undeliverable messages.                |
| Amazon SQS         | Unauthorized deletion or modification of messages | Medium  | IAM policies to restrict access; Enable SSE; Utilize SQS Queue policy.                           |
| Amazon SQS         | Message replay attacks                        | Low        | Implement unique message deduplication IDs; Enable API request authentication.                   |
| AWS Lambda         | Execution of malicious code                   | High       | Use least privilege IAM roles; Enable Lambda function concurrency controls.                     |
| AWS Lambda         | Vulnerable dependencies                       | High       | Regularly update Lambda functions with secure dependencies; Perform static code analysis.        |
| AWS S3 (Data Target)   | Data tampering                                 | Medium     | Enable versioning; Implement cross-region replication for redundancy; Access Controls.           |
| AWS S3 (Data Target)   | Insecure data at rest                         | Low        | Enable S3 Server-Side Encryption (SSE); Use encryption with customer-managed keys where possible.|
