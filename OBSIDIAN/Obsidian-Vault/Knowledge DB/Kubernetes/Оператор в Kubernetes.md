#kubernetes 

Оператор в [[Kubernetes]] — это концепция и методика, которая позволяет автоматизировать управление состоянием сложных приложений и ресурсов. Операторы облегчают управление состоянием приложений.

**Основные компоненты оператора**

🟠**Custom Resource Definitions (CRD):** CRD расширяют стандартные объекты Kubernetes, добавляя новые типы ресурсов. Эти ресурсы специфичны для приложений или сервисов, которыми управляет оператор.
🟠**Контроллер**: Контроллер — это программа, которая следит за состоянием ресурсов, определенных CRD, и выполняет действия для достижения желаемого состояния. Контроллеры пишутся на Go с использованием фреймворка Operator SDK.

**Зачем нужны операторы**

🟠**Автоматизация сложных задач**: Операторы автоматизируют рутинные задачи, такие как развертывание, обновление, резервное копирование и восстановление приложений, которые требуют знаний и вмешательства администратора.
🟠**Управление состоянием приложений**: Операторы следят за состоянием приложения и автоматически предпринимают действия для поддержания или восстановления этого состояния, обеспечивая высокую доступность и отказоустойчивость.
🟠**Интеграция с Kubernetes**: Операторы используют встроенные механизмы Kubernetes, такие как CRD и контроллеры, что позволяет легко интегрировать их в существующие кластеры Kubernetes и управлять приложениями в привычной среде.

**Примеры использования операторов**

🟠**Базы данных**: Оператор для PostgreSQL может автоматизировать задачи развертывания кластеров, настройки репликации, выполнения резервного копирования и восстановления.
🟠**Мониторинг и логирование**: Оператор для Prometheus может управлять развертыванием и настройкой экземпляров Prometheus, включая настройку сбора метрик и алертинга.
🟠**CI/CD**: Оператор для Jenkins может автоматизировать настройку мастера Jenkins и агентов, а также управлять плагинами и настройками.

**Определение CRD**

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: postgresqls.postgres.example.com
spec:
  group: postgres.example.com
  versions:
    - name: v1
      served: true
      storage: true
  scope: Namespaced
  names:
    plural: postgresqls
    singular: postgresql
    kind: PostgreSQL
    shortNames:
      - pg
```

**Разработка контроллера**

```go
func (r *ReconcilePostgreSQL) Reconcile(request reconcile.Request) (reconcile.Result, error) {
    instance := &v1alpha1.PostgreSQL{}
    err := r.client.Get(context.TODO(), request.NamespacedName, instance)
    if err != nil {
        return reconcile.Result{}, err
    }
   return reconcile.Result{}, nil
}
```

**Развертывание оператора**

```sh
operator-sdk init --domain example.com --repo github.com/example/postgresql-operator
operator-sdk create api --group postgres --version v1 --kind PostgreSQL --resource --controller
make install
make run
```