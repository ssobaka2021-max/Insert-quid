**Авторство: Хасанова Татьяна Ренатовна группа М3121**
  **Название плагина: Insert guid**
  # Описание плагина #
    __Описание__
    Guid Inserter - это расширение для Visual Studio 2022, которое позволяет быстро вставлять уникальные идентификаторы (GUID) в текстовый редактор с помощью одной кнопки в меню Edit.
    __Функциональность__
· Вставка нового GUID в позицию курсора
· Интеграция в меню Edit
· Простой и интуитивно понятный интерфейс
    __Использование__
1. Откройте любой текстовый файл в редакторе
2. Установите курсор в нужную позицию
3. Перейдите в меню Edit → Insert Guid
4. GUID будет автоматически вставлен в формате: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
   __Структура проекта__
   -InsertGuid
     _InserGuid.vsix
   -Properties
     _AssemblyInfo.cs
   -Ссылки
     _Анализаторы
     _System
     _System.ComponentModel.Composition
     _System.Design
   -Commands
     _MyCommand.cs
       _GuidInsertionHandler
   -Resources
     _Icon.png
   -InsertGuidPackage.cs
     _InsertGuidPackage
   -source.extension.vsixmanifest
     _source.extension.cs
   -VSCommandTable.vsct
   __Ход работы__
1. Подготовка среды разработки
2. Установка необходимых компонентов
3. Перед созданием плагина необходимо установить Extensibility Essentials - пакет расширений для разработки расширений Visual Studio. Этот пакет включает:
  · Шаблоны проектов для различных типов расширений
  · Инструменты отладки расширений
  · Библиотеки API для взаимодействия с IDE
  
4.Процесс установки:
    1. Открыть Visual Studio 2022
    2. Перейти в меню Extensions → Manage Extensions
    3. В поиске найти "Extensibility Essentials 2022"
    4. Установить и перезагрузить Visual Studio
5.Создание проекта расширения
    1. Выбор шаблона проекта
    При создании нового проекта выбираем шаблон "VSIX Project with Command" из категории Extensibility. Этот шаблон автоматически создает:
    · Файл проекта VSIX с настройками пакетирования
    · Командный обработчик для кнопки
    · Таблицу команд (VSCT) для определения элементов интерфейса
6.Конфигурация командного интерфейса
<Commands package="guidPackage">
  <Groups>
    -Группа команд в меню Edit-
    <Group guid="guidPackage" id="MyMenuGroup" priority="0x0600">
      -Родительское меню - раздел Edit главного меню-
      <Parent guid="guidSHLMainMenu" id="IDM_VS_MENU_EDIT"/>
    </Group>
  </Groups>

  <Buttons>
    -Определение нашей кнопки-
    <Button guid="guidPackage" id="MyCommand" priority="0x0100" type="Button">
      -Привязка к группе в меню Edit-
      <Parent guid="guidPackage" id="MyMenuGroup" />
      
      -Иконка кнопки - используется стандартная иконка "Вставить и добавить"-
      <Icon guid="ImageCatalogGuid" id="PasteAppend" />
      <CommandFlag>IconIsMoniker</CommandFlag>
      
      -Текстовые метки-
      <Strings>
        <ButtonText>Insert Guid</ButtonText>
        <ToolTip>Вставить новый GUID в позицию курсора</ToolTip>
        <CanonicalName>Edit.InsertGuid</CanonicalName>
        <LocCanonicalName>Edit: Insert Guid</LocCanonicalName>
      </Strings>
    </Button>
  </Buttons>
</Commands>

· <Groups>: Определяет группировку команд в меню
· <Parent guid="guidSHLMainMenu" id="IDM_VS_MENU_EDIT">: Указывает, что команда будет в меню Edit
· <Icon guid="ImageCatalogGuid" id="PasteAppend">: Использует стандартную иконку из каталога Visual Studio
· <CommandFlag>IconIsMoniker</CommandFlag>: Указывает, что иконка использует современную систему Moniker

Файл GuidInsertionHandler.cs - основной код плагина

Исправленная и комментированная версия кода:
using System;
using Community.VisualStudio.Toolkit;
using Microsoft.VisualStudio.Shell;
using Task = System.Threading.Tasks.Task;

namespace GuidInserter
{
    [Command(PackageIds.GuidInsertionCommand)]
    internal sealed class GuidInsertionHandler : BaseCommand<GuidInsertionHandler>
    {
        protected override async Task ExecuteAsync(OleMenuCmdEventArgs e)
        {
            // Переключаемся на главный поток UI - обязательно для работы с редактором
            await Package.JoinableTaskFactory.SwitchToMainThreadAsync();
            
            // Получаем активный документ в редакторе
            DocumentView activeDocument = await VS.Documents.GetActiveDocumentViewAsync();
            
            // Проверяем, что документ существует и доступен для редактирования
            if (activeDocument?.TextView == null) 
            {

            // Если нет активного редактора, показываем сообщение об ошибке
                await VS.MessageBox.ShowErrorAsync("Insert Guid", 
                    "Please open a text document first.");
                return;
            }
            
            // Получаем текущую позицию курсора в текстовом буфере
            SnapshotPoint cursorPosition = activeDocument.TextView.Caret.Position.BufferPosition;
            
            // Генерируем новый GUID и преобразуем в строку
            string newGuid = Guid.NewGuid().ToString();
            
            // Вставляем GUID в позицию курсора
            activeDocument.TextBuffer.Insert(cursorPosition, newGuid);
            
            // Опционально: показываем уведомление об успешной вставке
            await VS.StatusBar.ShowMessageAsync($"GUID inserted: {newGuid}");
        }
    }
}


1. Атрибут Command
[Command(PackageIds.GuidInsertionCommand)]

Связывает этот класс с командой, определенной в VSCT-файле. PackageIds.GuidInsertionCommand - это константа, содержащая идентификатор команды.

2. Наследование от BaseCommand
internal sealed class GuidInsertionHandler : BaseCommand<GuidInsertionHandler>

Базовый класс предоставляет инфраструктуру для работы с командами Visual Studio. sealed означает, что класс не может быть унаследован.

3. Метод ExecuteAsync
protected override async Task ExecuteAsync(OleMenuCmdEventArgs e)

Асинхронный метод, вызываемый при активации команды. Параметр e содержит информацию о контексте вызова команды.

4. Переключение на UI-поток
await Package.JoinableTaskFactory.SwitchToMainThreadAsync();

Критически важный момент: Все операции с элементами интерфейса должны выполняться в главном потоке. Этот вызов гарантирует, что код выполняется в правильном контексте.

5. Получение активного документа
DocumentView activeDocument = await VS.Documents.GetActiveDocumentViewAsync();

VS.Documents - сервис для работы с документами. Метод возвращает объект, представляющий активный текстовый редактор.

6. Проверка доступности редактора
if (activeDocument?.TextView == null) return;

· Документ существует (activeDocument не null)
· Доступен текстовый редактор (TextView не null)

8. Получение позиции курсора
SnapshotPoint cursorPosition = activeDocument.TextView.Caret.Position.BufferPosition;

Caret.Position.BufferPosition возвращает точную позицию курсора в текстовом буфере.

8. Генерация GUID
string newGuid = Guid.NewGuid().ToString();

Guid.NewGuid() создает новый уникальный идентификатор, который преобразуется в строку формата xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.

9. Вставка текста
activeDocument.TextBuffer.Insert(cursorPosition, newGuid);

TextBuffer представляет собой текстовое содержимое документа. Метод Insert добавляет текст в указанную позицию.

Настройка манифеста пакета

Файл Source.extension.vsixmanifest

Этот файл содержит метаданные расширения:
<PackageManifest>
  <Metadata>
    <Identity Id="GuidInserter.YourName.YourCompany" 
              Version="1.0" 
              Language="en-US" 
              Publisher="Your Name"/>
    <DisplayName>Guid Inserter</DisplayName>
    <Description>Плагин для быстрой вставки GUID в текстовый редактор</Description>
  </Metadata>
  
  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Community" Version="[17.0,18.0)"/>
  </Installation>
  
  <Dependencies>
    <Dependency Id="Microsoft.VisualStudio.MPF.17.0" DisplayName="Visual Studio MPF" Version="[17.0,18.0)"/>
  </Dependencies>
</PackageManifest>
   __Тестирование__
· Команда появляется в меню Edit
· Проверьте вставку GUID в различные типы файлов
· Протестируйте работу с большими файлами

  
  
  
