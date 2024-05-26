
const sidebar = {
  apisidebar: [
    {
      type: "doc",
      id: "reference/api/karrio-api",
    },
    {
      type: "category",
      label: "API",
      link: {
        type: "doc",
        id: "reference/api/api",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/ping",
          label: "Instance Metadata",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/data",
          label: "Data References",
          className: "api-method get",
        },
      ],
    },
    {
      type: "category",
      label: "Auth",
      link: {
        type: "doc",
        id: "reference/api/auth",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/authenticate",
          label: "Obtain auth token pair",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/refresh-token",
          label: "Refresh auth token",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/get-verified-token",
          label: "Get verified JWT token",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/verify-token",
          label: "Verify token",
          className: "api-method post",
        },
      ],
    },
    {
      type: "category",
      label: "Carriers",
      link: {
        type: "doc",
        id: "reference/api/carriers",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/list-carriers",
          label: "List all carriers",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/get-services",
          label: "Get carrier services",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/retrieve-carrier",
          label: "Retrieve a carrier account",
          className: "api-method get",
        },
      ],
    },
    {
      type: "category",
      label: "Addresses",
      link: {
        type: "doc",
        id: "reference/api/addresses",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/list-addresses",
          label: "List all addresses",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/create-address",
          label: "Create an address",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/retrieve-address",
          label: "Retrieve an address",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/update-address",
          label: "Update an address",
          className: "api-method patch",
        },
        {
          type: "doc",
          id: "reference/api/discard-address",
          label: "Discard an address",
          className: "api-method delete",
        },
      ],
    },
    {
      type: "category",
      label: "Parcels",
      link: {
        type: "doc",
        id: "reference/api/parcels",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/list-parcels",
          label: "List all parcels",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/create-parcel",
          label: "Create a parcel",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/retrieve-parcel",
          label: "Retrieve a parcel",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/update-parcel",
          label: "Update a parcel",
          className: "api-method patch",
        },
        {
          type: "doc",
          id: "reference/api/discard-parcel",
          label: "Remove a parcel",
          className: "api-method delete",
        },
      ],
    },
    {
      type: "category",
      label: "Shipments",
      link: {
        type: "doc",
        id: "reference/api/shipments",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/list-shipments",
          label: "List all shipments",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/create-shipment",
          label: "Create a shipment",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/retrieve-shipment",
          label: "Retrieve a shipment",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/update-shipment",
          label: "Update a shipment",
          className: "api-method put",
        },
        {
          type: "doc",
          id: "reference/api/cancel-shipment",
          label: "Cancel a shipment",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/purchase",
          label: "Buy a shipment label",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/rates",
          label: "Fetch new shipment rates",
          className: "api-method post",
        },
      ],
    },
    {
      type: "category",
      label: "Documents",
      link: {
        type: "doc",
        id: "reference/api/documents",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/generate-document",
          label: "Generate a document",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/list-document-templates",
          label: "List all templates",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/create-document-template",
          label: "Create a template",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/retrieve-document-template",
          label: "Retrieve a template",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/update-document-template",
          label: "Update a template",
          className: "api-method patch",
        },
        {
          type: "doc",
          id: "reference/api/discard-document-template",
          label: "Delete a template",
          className: "api-method delete",
        },
        {
          type: "doc",
          id: "reference/api/uploads",
          label: "List all upload records",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/upload",
          label: "Upload documents",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/retrieve-upload",
          label: "Retrieve upload record",
          className: "api-method get",
        },
      ],
    },
    {
      type: "category",
      label: "Manifests",
      link: {
        type: "doc",
        id: "reference/api/manifests",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/list-manifests",
          label: "List manifests",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/create-manifest",
          label: "Create a manifest",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/retrieve-manifest",
          label: "Retrieve a manifest",
          className: "api-method get",
        },
      ],
    },
    {
      type: "category",
      label: "Trackers",
      link: {
        type: "doc",
        id: "reference/api/trackers",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/list-trackers",
          label: "List all package trackers",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/add-tracker",
          label: "Add a package tracker",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/create-tracker",
          label: "Create a package tracker",
          className: "menu__list-item--deprecated api-method get",
        },
        {
          type: "doc",
          id: "reference/api/retrieve-tracker",
          label: "Retrieves a package tracker",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/update-tracker",
          label: "Update tracker data",
          className: "api-method put",
        },
        {
          type: "doc",
          id: "reference/api/remove-tracker",
          label: "Discard a package tracker",
          className: "api-method delete",
        },
      ],
    },
    {
      type: "category",
      label: "Pickups",
      link: {
        type: "doc",
        id: "reference/api/pickups",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/list-pickups",
          label: "List shipment pickups",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/schedule-pickup",
          label: "Schedule a pickup",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/retrieve-pickup",
          label: "Retrieve a pickup",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/update-pickup",
          label: "Update a pickup",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/cancel-pickup",
          label: "Cancel a pickup",
          className: "api-method post",
        },
      ],
    },
    {
      type: "category",
      label: "Proxy",
      link: {
        type: "doc",
        id: "reference/api/proxy",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/generate-manifest",
          label: "Create a manifest",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/pickup-schedule",
          label: "Schedule a pickup",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/pickup-cancel",
          label: "Cancel a pickup",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/pickup-update",
          label: "Update a pickup",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/fetch-rates",
          label: "Fetch shipment rates",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/buy-label",
          label: "Buy a shipment label",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/void-label",
          label: "Void a shipment label",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/get-tracking",
          label: "Get tracking details",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/track-shipment",
          label: "Track a shipment",
          className: "menu__list-item--deprecated api-method get",
        },
      ],
    },
    {
      type: "category",
      label: "Orders",
      link: {
        type: "doc",
        id: "reference/api/orders",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/list-orders",
          label: "List all orders",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/create-order",
          label: "Create an order",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/retrieve-order",
          label: "Retrieve an order",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/update-order",
          label: "Update an order",
          className: "api-method put",
        },
        {
          type: "doc",
          id: "reference/api/dismiss-order",
          label: "Dismiss an order",
          className: "menu__list-item--deprecated api-method delete",
        },
        {
          type: "doc",
          id: "reference/api/cancel-order",
          label: "Cancel an order",
          className: "api-method post",
        },
      ],
    },
    {
      type: "category",
      label: "Webhooks",
      link: {
        type: "doc",
        id: "reference/api/webhooks",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/list-webhooks",
          label: "List all webhooks",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/create-webhook",
          label: "Create a webhook",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/retrieve-webhook",
          label: "Retrieve a webhook",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/update-webhook",
          label: "Update a webhook",
          className: "api-method patch",
        },
        {
          type: "doc",
          id: "reference/api/remove-webhook",
          label: "Remove a webhook",
          className: "api-method delete",
        },
        {
          type: "doc",
          id: "reference/api/test-webhook",
          label: "Test a webhook",
          className: "api-method post",
        },
      ],
    },
    {
      type: "category",
      label: "Batches",
      link: {
        type: "doc",
        id: "reference/api/batches",
      },
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "reference/api/import-file",
          label: "Import data files",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/list-batch-operations",
          label: "List all batch operations",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/retrieve-batch-operation",
          label: "Retrieve a batch operation",
          className: "api-method get",
        },
        {
          type: "doc",
          id: "reference/api/create-orders",
          label: "Create order batch",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/create-shipments",
          label: "Create shipment batch",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "reference/api/create-trackers",
          label: "Create tracker batch",
          className: "api-method post",
        },
      ],
    },
  ],
};

export default sidebar.apisidebar;
