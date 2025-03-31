resource "aws_ecs_task_definition" "ocr_task" {
  family                   = "ocrmypdf-task"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.ecs_execution_role.arn
  cpu                      = "512"
  memory                   = "1024"
  container_definitions = jsonencode([{
    name      = "ocrmypdf"
    image     = "jbarlow83/ocrmypdf"
    essential = true
  }])
}
