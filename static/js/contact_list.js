document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('contact-search');
    const contactsBody = document.getElementById('contacts-body');
    const noResults = document.getElementById('no-results');

    // Function to add submit button to edit forms
    function addSubmitButton() {
        const form = document.querySelector('form');
        if (form && !form.querySelector('button[type="submit"]')) {
            const submitButton = document.createElement('button');
            submitButton.type = 'submit';
            submitButton.className = 'btn btn-primary';
            submitButton.textContent = 'Update Contact';
            form.appendChild(submitButton);
        }
    }

    // Call addSubmitButton on page load
    addSubmitButton();

    function renderContacts(contacts) {
        contactsBody.innerHTML = '';
        if (contacts.length === 0) {
            noResults.style.display = 'block';
        } else {
            noResults.style.display = 'none';
            contacts.forEach(contact => {
                const detailUrl = contact.type === 'Church' ? `/contacts/church/${contact.id}/` : `/contacts/person/${contact.id}/`;
                const editUrl = contact.type === 'Church' ? `/contacts/church/${contact.id}/edit/` : `/contacts/person/${contact.id}/edit/`;
                
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${contact.name}</td>
                    <td>${contact.type}</td>
                    <td>${contact.email}</td>
                    <td>${contact.phone}</td>
                    <td>${contact.last_contact}</td>
                    <td class="actions">
                        <a href="${detailUrl}" class="btn btn-sm btn-info">View</a>
                        <a href="${editUrl}" class="btn btn-sm btn-warning">Edit</a>
                    </td>
                `;
                contactsBody.appendChild(row);
            });
        }
    }

    function filterContacts(searchTerm) {
        if (!searchTerm) {
            renderContacts(contactsData);
            return;
        }

        const filtered = contactsData.filter(contact => {
            const searchFields = [
                contact.name,
                contact.type,
                contact.email,
                contact.phone,
                contact.last_contact,
                contact.person_type,
            ];
            return searchFields.some(field => 
                field && field.toLowerCase().includes(searchTerm.toLowerCase())
            );
        });
        renderContacts(filtered);
    }

    if (searchInput) {
        searchInput.addEventListener('input', function() {
            filterContacts(this.value);
        });

        // Initial render of all contacts
        if (typeof contactsData !== 'undefined' && Array.isArray(contactsData)) {
            renderContacts(contactsData);
        } else {
            console.error('contactsData is not defined or is not an array');
            noResults.style.display = 'block';
        }
    }
});