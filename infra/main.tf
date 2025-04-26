resource "aws_ecs_cluster" "cluster" {
  name = "tech-news-cluster"
}

resource "aws_ecs_task_definition" "scraper" {
  family                   = "tech-news-scraper"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = 256
  memory                   = 512
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([{
    name  = "web"
    image = "${aws_ecr_repository.tech_news.repository_url}:latest"
    portMappings = [{
      containerPort = 5000
      hostPort      = 5000
    }]
    environment = [
      { name = "DB_URL", value = "postgresql://avnadmin:${var.db_password}@${aws_db_instance.tech_news.endpoint}/tech_news" }
    ]
  }])
}