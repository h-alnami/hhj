# 🔐 الأمان والتحسين - Security & Optimization

**Nar Pic - Security Best Practices & Performance Optimization**

---

## 🔒 الأمان / Security

### حماية النماذج / Model Protection

```javascript
// 1. عدم السماح بالتنزيل المباشر
app.get('/models/:id', (req, res) => {
    // التحقق من المصادقة
    if (!req.user) return res.status(401).send('Unauthorized');
    
    // التحقق من الصلاحيات
    if (!hasPermission(req.user, 'models')) {
        return res.status(403).send('Forbidden');
    }
    
    // إرسال الملف بدون السماح بالتنزيل المباشر
    res.sendFile(modelPath, {
        headers: {
            'Content-Disposition': 'inline'
        }
    });
});

// 2. تشفير النماذج
const crypto = require('crypto');

function encryptModel(modelPath, encryptionKey) {
    const cipher = crypto.createCipher('aes-256-cbc', encryptionKey);
    const input = fs.createReadStream(modelPath);
    const output = fs.createWriteStream(modelPath + '.encrypted');
    
    input.pipe(cipher).pipe(output);
}

// 3. علامات مائية رقمية
function addDigitalWatermark(modelBuffer, metadata) {
    // إضافة معرّف فريد للنموذج
    const watermark = Buffer.from(JSON.stringify({
        owner: metadata.owner,
        timestamp: Date.now(),
        signature: metadata.signature
    }));
    
    return Buffer.concat([modelBuffer, watermark]);
}
```

### حماية البيانات / Data Protection

```python
# استخدام HTTPS
import ssl
from flask import Flask
from werkzeug.serving import WSGIRequestHandler

app = Flask(__name__)

# استخدام SSL Context
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('cert.pem', 'key.pem')

# تشفير البيانات الحساسة
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode()

# توثيق معلومات المستخدم
import jwt

def generate_token(user_id, secret_key):
    return jwt.encode(
        {'user_id': user_id, 'exp': datetime.utcnow() + timedelta(hours=24)},
        secret_key,
        algorithm='HS256'
    )

@app.route('/api/models')
def get_models():
    token = request.headers.get('Authorization')
    try:
        user = jwt.decode(token.split(' ')[1], SECRET_KEY, algorithms=['HS256'])
        # السماح بالوصول
    except jwt.ExpiredSignatureError:
        return {'error': 'Token expired'}, 401
```

### معايير الأمان / Security Standards

```
✅ Use HTTPS only
✅ Implement JWT authentication
✅ Validate all inputs
✅ Sanitize outputs
✅ Use strong passwords
✅ Implement rate limiting
✅ Log security events
✅ Regular security audits
```

---

## ⚡ التحسينات / Optimization

### تحسين الأداء / Performance

#### 1. ضغط النماذج

```python
def compress_model(input_path, output_path, quality=0.9):
    """ضغط نموذج GLB مع الحفاظ على الجودة"""
    import trimesh
    
    # تحميل النموذج
    mesh = trimesh.load(input_path)
    
    # تقليل المضلعات
    mesh = mesh.simplify_mesh(
        target_reduction=1 - quality
    )
    
    # ضغط الملمس
    # ... texture compression
    
    # حفظ النموذج المضغوط
    mesh.export(output_path, file_type='glb')
```

#### 2. Lazy Loading

```javascript
// تحميل النماذج عند الطلب
class LazyModelLoader {
    constructor() {
        this.cache = new Map();
    }
    
    async loadModel(modelId) {
        // تحقق من الـ Cache
        if (this.cache.has(modelId)) {
            return this.cache.get(modelId);
        }
        
        // تحميل من الخادم
        const model = await fetch(`/api/models/${modelId}`)
            .then(res => res.arrayBuffer())
            .then(buffer => this.parseGLB(buffer));
        
        // حفظ في الـ Cache
        this.cache.set(modelId, model);
        
        return model;
    }
}
```

#### 3. CDN Integration

```javascript
// استخدام CDN للنماذج
const CDN_URL = 'https://cdn.example.com/models';

function getModelUrl(modelId, format = 'glb') {
    return `${CDN_URL}/${modelId}.${format}`;
}

// مع Caching Headers
app.use('/models', (req, res, next) => {
    // Cache for 7 days
    res.setHeader('Cache-Control', 'public, max-age=604800');
    next();
});
```

#### 4. Progressive Enhancement

```html
<!-- تحميل تدريجي -->
<div id="model-container">
    <canvas id="loading-screen"></canvas>
    <script>
        // عرض شاشة التحميل
        showLoadingScreen();
        
        // تحميل النموذج في الخلفية
        loadModelAsync('model-id')
            .then(model => {
                hideLoadingScreen();
                renderModel(model);
            });
    </script>
</div>
```

---

## 📊 مراقبة الأداء / Performance Monitoring

### قياس الأداء

```javascript
class PerformanceMonitor {
    constructor() {
        this.metrics = {};
    }
    
    measureLoadTime(modelId) {
        const startTime = performance.now();
        
        loadModel(modelId).then(() => {
            const loadTime = performance.now() - startTime;
            
            this.metrics[modelId] = {
                loadTime,
                timestamp: new Date(),
                size: getModelSize(modelId),
                memoryUsage: getMemoryUsage()
            };
            
            // إرسال إلى Analytics
            this.reportMetrics();
        });
    }
    
    reportMetrics() {
        console.log('Performance Metrics:', this.metrics);
        
        // إرسال إلى خادم التحليلات
        fetch('/api/analytics/performance', {
            method: 'POST',
            body: JSON.stringify(this.metrics)
        });
    }
}
```

### استهدافات الأداء / Performance Targets

```
Load Time: < 3 seconds
Memory Usage: < 500MB
Frame Rate: 60+ FPS
Battery Impact: < 5% per hour
Bandwidth: < 50MB per model
```

---

## 🖼️ تحسينات الملمس / Texture Optimization

```glsl
// استخدام Compressed Textures
// ASTC, ETC2, PVRTC

#ifdef COMPRESSED_TEXTURES
    uniform sampler2D astcTexture;
    
    vec4 textureSample = texture(astcTexture, uv);
#else
    uniform sampler2D standardTexture;
    
    vec4 textureSample = texture(standardTexture, uv);
#endif
```

---

## 🔧 تكوين الخادم / Server Configuration

### Nginx Configuration

```nginx
server {
    listen 443 ssl http2;
    server_name api.example.com;
    
    # SSL Configuration
    ssl_certificate /etc/ssl/cert.pem;
    ssl_certificate_key /etc/ssl/key.pem;
    ssl_protocols TLSv1.3 TLSv1.2;
    ssl_ciphers HIGH:!aNULL:!MD5;
    
    # Compression
    gzip on;
    gzip_types application/json application/octet-stream;
    gzip_min_length 1000;
    gzip_comp_level 6;
    
    # Caching
    location /models/ {
        expires 7d;
        add_header Cache-Control "public, immutable";
    }
    
    # Rate Limiting
    limit_req_zone $binary_remote_addr zone=api:10m rate=100r/m;
    limit_req zone=api burst=20 nodelay;
    
    # Security Headers
    add_header Strict-Transport-Security "max-age=31536000";
    add_header X-Content-Type-Options "nosniff";
    add_header X-Frame-Options "DENY";
}
```

---

## 📈 Scaling & Load Balancing

### Docker Deployment

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
    CMD node healthcheck.js

CMD ["node", "server.js"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "3000:3000"
    environment:
      NODE_ENV: production
      DB_URL: postgres://db:5432/rakan
    depends_on:
      - db
    restart: always
    deploy:
      replicas: 3  # مثيلات متعددة

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: rakan
      POSTGRES_PASSWORD: secure_password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    # للـ Caching

volumes:
  postgres_data:
```

---

## 🔍 Monitoring & Logging

```python
import logging
from pythonjsonlogger import jsonlogger

# إعداد Logging
logger = logging.getLogger(__name__)
handler = logging.FileHandler('app.log')
formatter = jsonlogger.JsonFormatter()
handler.setFormatter(formatter)
logger.addHandler(handler)

# تسجيل الأحداث
@app.before_request
def log_request():
    logger.info('Request', extra={
        'method': request.method,
        'path': request.path,
        'ip': request.remote_addr
    })

@app.after_request
def log_response(response):
    logger.info('Response', extra={
        'status': response.status_code,
        'duration': time.time() - request.start_time
    })
```

---

## 🚀 DevOps Best Practices

### CI/CD Pipeline

```yaml
name: Security & Performance

on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Security Scan
        run: |
          npm install -g snyk
          snyk test
      
      - name: SAST Analysis
        run: |
          npm install -g semgrep
          semgrep --config=p/security-audit .
      
      - name: Dependency Check
        run: npm audit

  performance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build
        run: npm run build
      
      - name: Performance Test
        run: npm run test:performance
      
      - name: Size Analysis
        run: npm run analyze:size
```

---

## 📋 Security Checklist

```
Authentication:
  ☐ Implement JWT tokens
  ☐ Use secure password hashing
  ☐ Implement 2FA (optional)

Authorization:
  ☐ Role-based access control
  ☐ Principle of least privilege
  ☐ Regular permission audits

Data Protection:
  ☐ Encrypt sensitive data
  ☐ Use HTTPS only
  ☐ Implement rate limiting
  ☐ Input validation

Monitoring:
  ☐ Security event logging
  ☐ Intrusion detection
  ☐ Regular backups
  ☐ Incident response plan
```

---

**آخر تحديث:** 2026-08-28
