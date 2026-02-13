variable "region" {
  description = "AWS Region"
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "EKS Cluster Name"
  default     = "poc13-eks-cluster"
}

variable "node_instance_type" {
  description = "EC2 Instance Type for Worker Nodes"
  default     = "t3.medium"
}
