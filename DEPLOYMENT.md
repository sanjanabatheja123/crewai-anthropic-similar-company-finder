# Production Deployment Guide

This guide covers deploying the Similar Company Finder Crew to production using Anthropic's Claude models.

## Prerequisites

1. **Anthropic API Key**: Get your API key from [Anthropic Console](https://console.anthropic.com/)
2. **Serper API Key** (optional): For web search functionality from [Serper](https://serper.dev/)
3. **Docker** (recommended): For containerized deployment
4. **Python 3.10-3.13**: If running without Docker

## Environment Configuration

### Required Environment Variables

```bash
# Required
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Optional but recommended
SERPER_API_KEY=your_serper_api_key_here
TARGET_COMPANY=your_target_company_name
OUR_PRODUCT=your_product_description

# Production settings
ENVIRONMENT=production
LOG_LEVEL=INFO
CREWAI_TELEMETRY_OPT_OUT=true
```

## Deployment Options

### Option 1: Docker Deployment (Recommended)

1. **Build and run with Docker Compose:**
   ```bash
   # Copy environment variables
   cp .env.example .env
   # Edit .env with your actual API keys
   
   # Build and start the service
   docker-compose up -d --build
   ```

2. **View logs:**
   ```bash
   docker-compose logs -f similar-company-finder
   ```

3. **Stop the service:**
   ```bash
   docker-compose down
   ```

### Option 2: Direct Python Deployment

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Set environment variables:**
   ```bash
   export ANTHROPIC_API_KEY="your_key_here"
   export SERPER_API_KEY="your_key_here"
   export TARGET_COMPANY="Company Name"
   export OUR_PRODUCT="Product Description"
   ```

3. **Run the crew:**
   ```bash
   uv run similar_company_finder_template
   ```

### Option 3: Cloud Deployment

#### AWS ECS/Fargate
1. Push Docker image to ECR
2. Create ECS task definition with environment variables
3. Deploy as ECS service

#### Google Cloud Run
1. Build and push to Google Container Registry
2. Deploy with environment variables configured

#### Azure Container Instances
1. Push to Azure Container Registry
2. Deploy with environment configuration

## Production Considerations

### Security
- Store API keys in secure secret management (AWS Secrets Manager, Azure Key Vault, etc.)
- Use IAM roles instead of hardcoded credentials where possible
- Enable container scanning for vulnerabilities

### Monitoring
- Set up logging aggregation (ELK stack, CloudWatch, etc.)
- Monitor API usage and costs
- Set up alerts for failures

### Scaling
- Configure horizontal scaling based on workload
- Consider using message queues for batch processing
- Implement rate limiting for API calls

### Cost Optimization
- Monitor Anthropic API usage
- Implement caching for repeated queries
- Use appropriate Claude model for your use case:
  - `claude-3-5-sonnet-20241022`: Best performance (current default)
  - `claude-3-haiku-20240307`: Faster, more cost-effective for simpler tasks

## Configuration Tuning

### Model Selection
Edit `src/similar_company_finder_template/crew.py` to change the Claude model:

```python
def _get_anthropic_llm(self):
    return ChatAnthropic(
        model="claude-3-haiku-20240307",  # Change model here
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        temperature=0.1,
        max_tokens=4096,
    )
```

### Temperature Settings
- `0.0-0.2`: More deterministic, consistent results (recommended for production)
- `0.3-0.7`: Balanced creativity and consistency
- `0.8-1.0`: More creative but less predictable

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify ANTHROPIC_API_KEY is set correctly
   - Check API key permissions and billing status

2. **Rate Limiting**
   - Implement exponential backoff
   - Monitor API usage in Anthropic Console

3. **Memory Issues**
   - Increase container memory limits
   - Optimize agent configurations

4. **Network Timeouts**
   - Configure appropriate timeout values
   - Implement retry logic

### Health Checks

Add health check endpoints for production monitoring:

```python
# Add to main.py
def health_check():
    """Simple health check endpoint"""
    try:
        # Test Anthropic connection
        llm = ChatAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        return {"status": "healthy", "timestamp": datetime.now().isoformat()}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
```

## Support

For production support:
- Check [CrewAI Documentation](https://docs.crewai.com)
- Review [Anthropic API Documentation](https://docs.anthropic.com)
- Monitor system logs and metrics
