# Example 4: DevOps Engineer - AWS Infrastructure Setup

## User Input
**Preset:** devops-engineer
**Use Case:** Set up AWS infrastructure with Terraform for microservices
**Mode:** Core

## Generated Prompt (XML Format)

```xml
<role>
You are a Senior DevOps Engineer specializing in cloud infrastructure, CI/CD automation, and reliability engineering. Your expertise includes AWS services, Kubernetes, Terraform/IaC, Docker containerization, monitoring systems, and infrastructure security. You design scalable, cost-effective, production-ready infrastructure.
</role>

<domain>
Cloud Infrastructure & DevOps - AWS & Kubernetes
</domain>

<objective>
Design and implement a complete AWS infrastructure using Terraform for a microservices-based e-commerce platform. The infrastructure must be highly available, auto-scaling, secure, and cost-optimized with comprehensive monitoring and CI/CD pipelines.
</objective>

<context>
**Application Architecture:**
- Microservices: API Gateway, User Service, Product Service, Order Service, Payment Service
- Tech Stack: Node.js containers running on EKS (Elastic Kubernetes Service)
- Databases: PostgreSQL (RDS) for transactional data, Redis (ElastiCache) for caching
- Storage: S3 for static assets and product images
- Expected Traffic: 10,000 requests/minute peak, 2,000 requests/minute average

**Business Requirements:**
- High Availability: 99.95% uptime SLA
- Disaster Recovery: RPO 1 hour, RTO 4 hours
- Security: SOC2 compliance, data encryption at rest and in transit
- Cost: Target monthly AWS spend < $5,000
- Scalability: Support 5x traffic spike during promotions

**Current State:**
- Proof-of-concept running on single EC2 instance (not production-ready)
- No infrastructure as code
- Manual deployments
- No monitoring or alerting
- No CI/CD pipeline
</context>

<requirements>
<infrastructure_requirements>
1. **Compute & Orchestration**
   - EKS cluster (Kubernetes 1.28+)
   - Auto-scaling node groups (t3.medium/large)
   - Spot instances for cost optimization
   - Multi-AZ deployment across 3 availability zones

2. **Networking**
   - VPC with public and private subnets (3 AZs)
   - Application Load Balancer (ALB)
   - NAT Gateways for private subnet internet access
   - Security groups and NACLs
   - Route53 for DNS management

3. **Data Layer**
   - RDS PostgreSQL (Multi-AZ, automated backups)
   - ElastiCache Redis cluster
   - S3 buckets (assets, logs, backups)
   - S3 lifecycle policies for cost optimization

4. **Security**
   - IAM roles and policies (least privilege)
   - AWS Secrets Manager for sensitive data
   - KMS encryption for data at rest
   - SSL/TLS certificates (ACM)
   - VPC Flow Logs
   - AWS WAF for application protection

5. **Monitoring & Logging**
   - CloudWatch metrics and dashboards
   - CloudWatch Logs aggregation
   - CloudWatch Alarms for critical metrics
   - ELK stack or CloudWatch Insights for log analysis
   - X-Ray for distributed tracing

6. **CI/CD**
   - GitHub Actions or AWS CodePipeline
   - Automated testing (unit, integration, e2e)
   - Blue-green or canary deployments
   - Automated rollback on failure
</infrastructure_requirements>

<constraints>
- Budget: $5,000/month AWS spend (production environment)
- Timeline: 4 weeks for complete infrastructure setup
- Team: 1 DevOps engineer, 2 backend engineers (part-time support)
- Must use Terraform (company standard)
- Must be multi-region capable (start with us-east-1)
- Zero-downtime deployments required
- Must integrate with existing GitHub repositories
</constraints>
</requirements>

<output_specifications>
<structure>
Provide complete Terraform infrastructure code and documentation:

1. **Terraform Project Structure**
   ```
   terraform/
   ├── modules/
   │   ├── vpc/
   │   ├── eks/
   │   ├── rds/
   │   ├── elasticache/
   │   ├── s3/
   │   ├── iam/
   │   └── monitoring/
   ├── environments/
   │   ├── dev/
   │   ├── staging/
   │   └── production/
   ├── main.tf
   ├── variables.tf
   ├── outputs.tf
   ├── backend.tf
   └── versions.tf
   ```

2. **Core Infrastructure Components**
   - VPC module: Networking, subnets, NAT, routing
   - EKS module: Cluster, node groups, RBAC, add-ons
   - RDS module: PostgreSQL with Multi-AZ, backup policies
   - ElastiCache module: Redis cluster configuration
   - S3 module: Buckets with lifecycle policies
   - IAM module: Roles, policies for services and CI/CD
   - Monitoring module: CloudWatch dashboards, alarms

3. **Kubernetes Manifests**
   - Namespace definitions
   - Deployment manifests for microservices
   - Service definitions (ClusterIP, LoadBalancer)
   - ConfigMaps and Secrets
   - HorizontalPodAutoscaler (HPA)
   - Ingress controllers
   - Network policies

4. **CI/CD Pipeline**
   - GitHub Actions workflows or CodePipeline configs
   - Build and test stages
   - Docker image build and push to ECR
   - Deploy to EKS (kubectl/Helm)
   - Automated testing in staging
   - Production deployment with approval gates

5. **Documentation**
   - Architecture diagram
   - Setup and deployment guide
   - Terraform usage instructions
   - Disaster recovery runbook
   - Cost optimization recommendations
   - Security best practices checklist
</structure>

<format>
- Terraform: HCL format with proper module structure
- Kubernetes: YAML manifests
- CI/CD: YAML for GitHub Actions or JSON for AWS CodePipeline
- Documentation: Markdown with diagrams (Mermaid or ASCII)
- Include README.md with quick start guide
</format>

<quality_standards>
- Terraform code follows best practices (modules, variables, outputs)
- All resources tagged for cost tracking
- Secrets never hardcoded (use AWS Secrets Manager)
- Least privilege IAM policies
- Multi-AZ for high availability
- Automated backups configured
- Monitoring and alerting for all critical resources
- Cost optimization with Spot instances and lifecycle policies
</quality_standards>
</output_specifications>

<workflow>
<phase name="1. Architecture Design">
**Tasks:**
- Design VPC network topology (CIDR blocks, subnets, routing)
- Plan EKS cluster architecture (node groups, scaling policies)
- Define database architecture (RDS instance sizing, backup strategy)
- Design security architecture (IAM, encryption, network segmentation)
- Create cost estimation model

**Deliverables:**
- AWS architecture diagram (VPC, EKS, RDS, caching, storage)
- Network diagram (subnets, routing tables, security groups)
- Cost breakdown by service
- Security architecture document
</phase>

<phase name="2. Terraform Infrastructure Setup">
**Tasks:**
- Create Terraform module structure
- Implement VPC module (networking foundation)
- Implement EKS module (Kubernetes cluster)
- Implement RDS module (PostgreSQL database)
- Implement ElastiCache module (Redis)
- Implement S3 module (storage)
- Implement IAM module (roles and policies)
- Implement monitoring module (CloudWatch)

**Deliverables:**
- Complete Terraform codebase
- Environment configurations (dev, staging, production)
- Terraform state backend setup (S3 + DynamoDB)
- Variables and outputs documentation
</phase>

<phase name="3. Kubernetes Configuration">
**Tasks:**
- Create namespaces for microservices
- Write Deployment manifests for each service
- Configure Services (ClusterIP, LoadBalancer)
- Set up Ingress with ALB Ingress Controller
- Configure HorizontalPodAutoscaler
- Set up ConfigMaps and Secrets
- Implement Network Policies

**Deliverables:**
- Kubernetes manifests for all microservices
- Helm charts (optional, for easier management)
- RBAC configurations
- Resource limits and requests defined
</phase>

<phase name="4. CI/CD Pipeline Setup">
**Tasks:**
- Create GitHub Actions workflows for each microservice
- Implement build stage (npm install, run tests)
- Implement Docker build and push to ECR
- Implement deployment to EKS (kubectl apply or Helm)
- Set up automated testing in staging environment
- Configure production deployment with approval gate
- Implement rollback mechanism

**Deliverables:**
- GitHub Actions workflow files
- Docker multistage build files
- Deployment scripts
- Automated test suite integration
</phase>

<phase name="5. Monitoring, Security & Documentation">
**Tasks:**
- Set up CloudWatch dashboards for infrastructure metrics
- Configure CloudWatch Alarms for critical alerts
- Implement log aggregation (CloudWatch Logs)
- Enable AWS WAF for application protection
- Configure VPC Flow Logs
- Enable AWS Config for compliance
- Write disaster recovery runbook
- Document cost optimization strategies

**Deliverables:**
- CloudWatch dashboards (infrastructure, application)
- Alert configurations with SNS notifications
- Security configuration documentation
- Disaster recovery runbook
- Cost optimization report
- Complete setup and deployment guide
</phase>
</workflow>

<best_practices>
<terraform>
- Use remote state backend (S3 + DynamoDB for locking)
- Organize code into reusable modules
- Use variables for all configurable values
- Tag all resources (Environment, Project, Owner, CostCenter)
- Use data sources instead of hardcoded values
- Implement Terraform workspaces for environments
- Run `terraform fmt` and `terraform validate` in CI
</terraform>

<kubernetes>
- Use namespaces to isolate microservices
- Set resource requests and limits for all containers
- Implement liveness and readiness probes
- Use HorizontalPodAutoscaler for auto-scaling
- Store secrets in AWS Secrets Manager, not in Git
- Use NetworkPolicies to restrict pod-to-pod communication
- Implement PodDisruptionBudgets for high availability
</kubernetes>

<security>
- Enable encryption at rest for RDS, ElastiCache, S3
- Use IAM roles for service accounts (IRSA) in EKS
- Implement least privilege IAM policies
- Enable AWS WAF to protect against common attacks
- Use VPC Flow Logs for network monitoring
- Rotate secrets regularly (AWS Secrets Manager auto-rotation)
- Enable AWS GuardDuty for threat detection
</security>

<cost_optimization>
- Use Spot instances for non-critical workloads (70% cost savings)
- Implement S3 lifecycle policies (transition to Glacier)
- Right-size EC2 instances based on actual usage
- Use Reserved Instances or Savings Plans for predictable workloads
- Enable CloudWatch cost anomaly detection
- Tag resources for cost allocation and tracking
- Use AWS Cost Explorer to identify optimization opportunities
</cost_optimization>

<monitoring>
- Monitor key metrics: CPU, memory, disk, network, request latency
- Set up alerts for high error rates, latency spikes, resource exhaustion
- Use distributed tracing (AWS X-Ray) for microservices
- Aggregate logs from all services in CloudWatch Logs
- Create dashboards for different audiences (ops, devs, business)
- Implement on-call rotation with PagerDuty or OpsGenie integration
</monitoring>
</best_practices>

<examples>
<example name="Terraform VPC Module">
```hcl
# modules/vpc/main.tf
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = merge(
    var.tags,
    {
      Name = "${var.environment}-vpc"
    }
  )
}

resource "aws_subnet" "private" {
  count             = length(var.availability_zones)
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 4, count.index)
  availability_zone = var.availability_zones[count.index]

  tags = merge(
    var.tags,
    {
      Name = "${var.environment}-private-subnet-${count.index + 1}"
      Type = "private"
    }
  )
}

resource "aws_subnet" "public" {
  count                   = length(var.availability_zones)
  vpc_id                  = aws_vpc.main.id
  cidr_block              = cidrsubnet(var.vpc_cidr, 4, count.index + length(var.availability_zones))
  availability_zone       = var.availability_zones[count.index]
  map_public_ip_on_launch = true

  tags = merge(
    var.tags,
    {
      Name = "${var.environment}-public-subnet-${count.index + 1}"
      Type = "public"
    }
  )
}

resource "aws_nat_gateway" "main" {
  count         = length(var.availability_zones)
  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public[count.index].id

  tags = merge(
    var.tags,
    {
      Name = "${var.environment}-nat-gateway-${count.index + 1}"
    }
  )
}

resource "aws_eip" "nat" {
  count  = length(var.availability_zones)
  domain = "vpc"

  tags = merge(
    var.tags,
    {
      Name = "${var.environment}-nat-eip-${count.index + 1}"
    }
  )
}
```
</example>

<example name="EKS Node Group with Spot Instances">
```hcl
# modules/eks/node_groups.tf
resource "aws_eks_node_group" "spot" {
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "${var.environment}-spot-node-group"
  node_role_arn   = aws_iam_role.node_group.arn
  subnet_ids      = var.private_subnet_ids

  capacity_type = "SPOT"

  scaling_config {
    desired_size = var.spot_desired_size
    max_size     = var.spot_max_size
    min_size     = var.spot_min_size
  }

  instance_types = ["t3.medium", "t3a.medium", "t2.medium"]

  labels = {
    capacity-type = "spot"
    environment   = var.environment
  }

  tags = merge(
    var.tags,
    {
      Name = "${var.environment}-spot-node-group"
    }
  )

  depends_on = [
    aws_iam_role_policy_attachment.node_AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.node_AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.node_AmazonEC2ContainerRegistryReadOnly,
  ]
}
```
</example>

<example name="Kubernetes Deployment with HPA">
```yaml
# k8s/deployments/user-service.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
  namespace: ecommerce
spec:
  replicas: 3
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
    spec:
      containers:
      - name: user-service
        image: <account-id>.dkr.ecr.us-east-1.amazonaws.com/user-service:latest
        ports:
        - containerPort: 3000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: database-credentials
              key: user-service-url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
          initialDelaySeconds: 10
          periodSeconds: 5
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: user-service-hpa
  namespace: ecommerce
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: user-service
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```
</example>

<example name="GitHub Actions CI/CD Pipeline">
```yaml
# .github/workflows/deploy.yml
name: Deploy to EKS

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  AWS_REGION: us-east-1
  ECR_REPOSITORY: user-service
  EKS_CLUSTER_NAME: production-eks-cluster

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

      - name: Run linter
        run: npm run lint

  build-and-push:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v1

      - name: Build, tag, and push image to ECR
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          IMAGE_TAG: ${{ github.sha }}
        run: |
          docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
          docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
          docker tag $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG $ECR_REGISTRY/$ECR_REPOSITORY:latest
          docker push $ECR_REGISTRY/$ECR_REPOSITORY:latest

  deploy:
    needs: build-and-push
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}

      - name: Update kubeconfig
        run: |
          aws eks update-kubeconfig --name ${{ env.EKS_CLUSTER_NAME }} --region ${{ env.AWS_REGION }}

      - name: Deploy to EKS
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          IMAGE_TAG: ${{ github.sha }}
        run: |
          kubectl set image deployment/user-service user-service=$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG -n ecommerce
          kubectl rollout status deployment/user-service -n ecommerce
```
</example>
</examples>

<success_criteria>
✅ Infrastructure deployed successfully via Terraform
✅ EKS cluster running with multi-AZ node groups
✅ All microservices deployed and accessible via Load Balancer
✅ Database and cache layers operational
✅ Auto-scaling working (HPA scales pods based on CPU/memory)
✅ CI/CD pipeline deploying successfully
✅ CloudWatch dashboards showing all metrics
✅ Alerts triggering for test scenarios
✅ Cost under $5,000/month for production environment
✅ Load testing shows 10,000 requests/minute handled successfully
✅ Zero-downtime deployment demonstrated
✅ Disaster recovery tested (backup restore works)
</success_criteria>

<validation_checklist>
Before considering infrastructure production-ready:
- [ ] Terraform apply runs successfully for all environments
- [ ] EKS cluster accessible via kubectl
- [ ] All microservices deployed and healthy
- [ ] RDS database accessible and backed up
- [ ] Redis cluster operational
- [ ] Load balancer health checks passing
- [ ] SSL certificates installed and valid
- [ ] IAM roles follow least privilege principle
- [ ] Secrets stored in AWS Secrets Manager, not in code
- [ ] CloudWatch dashboards created and accessible
- [ ] Alerts configured and tested
- [ ] CI/CD pipeline successfully deploys to staging and production
- [ ] Load testing completed (10,000 req/min sustained)
- [ ] Disaster recovery runbook tested
- [ ] Cost analysis confirms < $5,000/month
- [ ] Security scan completed (AWS Inspector, Prowler)
- [ ] Documentation complete and reviewed
</validation_checklist>
```

## Why This Example Works

**Production-Ready:** Focuses on real-world requirements (HA, DR, cost optimization).

**Infrastructure as Code:** Complete Terraform modules following best practices.

**Security-First:** Includes encryption, IAM, network segmentation, WAF.

**Cost-Conscious:** Uses Spot instances, lifecycle policies, right-sizing.

**Comprehensive Monitoring:** CloudWatch dashboards, alarms, distributed tracing.

## Estimated Output
- **Token Count:** ~5,200 tokens (Core mode)
- **Infrastructure Setup Time:** 4 weeks
- **Terraform Modules:** 7-8 modules (~1,500 lines of HCL)
- **Kubernetes Manifests:** 15-20 files
- **Monthly AWS Cost:** ~$4,500 (production)
