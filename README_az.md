
# Sığorta Sifarişi İdarəetmə Sistemi

Bu layihə istifadəçilərə qeydiyyatdan keçmək, hesablarına daxil olmaq, aktiv məhsullara baxmaq, sifariş yaratmaq və sifarişin statusunu yoxlamaq imkanı verən bir sığorta xidmətidir.


### Proyekti Klonlayın

```bash
git clone https://github.com/ismayilibrahimov/insurance-order-management-system.git
```

### Mühit Tənzimləməsi

1. Proyektin daxilində `.env` faylı yaradın.
2. `.env` faylına aşağıdakı dəyişənləri əlavə edin.

```bash
POSTGRES_DB=insurance
POSTGRES_USER=postgres
POSTGRES_PASSWORD=root
DB_HOST=db
DB_PORT=5432
```

### Docker Konteynerlərini Qurun və İşə Salın

```bash
docker compose up --build
```

### Super İstifadəçi Yaradın
Konteynerlər işə düşdükdən sonra tətbiqi idarə etmək üçün super istifadəçi yaradın:

```bash
docker compose exec web python manage.py createsuperuser
```

### Məhsullar Yaradın (Django admin panelində)
Super istifadəçi yaratdıqdan sonra aşağıdakı məhsulları yarada bilərsiniz:
- Avto Sığorta
- Sağlamlıq Sığortası

## API Endpoints

### Aktiv Məhsullar
- **Endpoint**: `/api/v1/products/`
- **Method**: `GET`

### İstifadəçi qeydiyyatı
- **Endpoint**: `/api/v1/signup/`
- **Method**: `POST`
- **Payload**:

```json
{
  "username": "test",
  "email": "test@example.com",
  "password": "test"
}
```

### Login
- **Endpoint**: `/api/v1/login/`
- **Method**: `POST`
- **Payload**:
```json
{
  "username": "test",
  "password": "test"
}
```

### İstifadəçi sifarişləri
- **Endpoint**: `/api/v1/orders/`
- **Method**: `GET`
- **Authorization**: Authorization header-də Bearer Token olmalıdır.

### Sifarişin yaradılması
- **Endpoint**: `/api/v1/order/create/`
- **Method**: `POST`
- **Authorization**: Authorization header-də Bearer Token olmalıdır.
- **Payload**:
```json
{
  "product": 1
}
```

### Sifarişin statusu haqqında məlumat
- **Endpoint**: `/api/v1/order/<int:pk>/status/`
- **Method**: `GET`
- **Authorization**: Authorization header-də Bearer Token olmalıdır.


## İstifadəçi Rolları
- **Super İstifadəçi**: Yalnız super İstifadəçi digər istifadəçilərin (admin və ya adi istifadəçi) rollarını dəyişə bilər.
- **Admin İstifadəçi**: Məhsulları və sifarişləri görə və redaktə edə bilər. (Django admin paneli vasitəsilə)
- **Adi İstifadəçi**: Yalnız öz sifarişlərini görə və yarada bilər. (API endpointləri vasitəsilə)

## Unit Testlərin İcrası
```bash
docker compose exec web python manage.py test
```
